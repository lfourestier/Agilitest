# Author Luc Fourestier (luc.fourestier@gmail.com)
#

import os
import os.path
import re
import TestGlobal
import Log
from TestSuite import TestSuite
from TestCase import TestCase
from TestResult import TestResult
import subprocess
import shlex

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Test suite file recognition
GTEST_EXT = "TestSuite.cpp"
JUNIT_EXT = "TestSuite.java"
CPPUNIT_EXT = "TestSuite.cpp"
CUNIT_EXT = "TestSuite.c"

# Commands
COMMAND_LIST = [TestGlobal.GTEST_TYPE, TestGlobal.JUNIT_TYPE, TestGlobal.CPPUNIT_TYPE, TestGlobal.CUNIT_TYPE]
COMMAND_COMMAND = "command"
COMMAND_RESULT = "result"
COMMAND_DEFAULT_RESULT = "Result.xml"
COMMAND_DELIMITER = "@@"
COMMAND_SUITE = "@SUITE"
COMMAND_CASE = "@CASE"

# Reg Exp

GTEST_SUITE_REGEXP = "@defgroup.*?@\{"
GTEST_CASE_REGEXP_LIST = ["(@test.*?)TEST_F\((\w+)\s*,\s*(\w+)\)", "(@test.*?)TEST\((\w+)\s*,\s*(\w+)\)"]

JUNIT_SUITE_REGEXP = "@defgroup.*?@\{"
JUNIT_CASE_REGEXP_LIST = ["(@test.*?)@Test.*?(test\w+)\s*\("]

# The test bench class that provides test management functions
class TestBench:
    def __init__(self, dir_list, commands, report_file, synthesis_file):
        self.dir_list = dir_list  # As list
        self.commands = commands  # As dictionary {gtest:blabla, junit:sdfsdf, ...}
        self.report_file = report_file
        self.synthesis_file = synthesis_file
        
        self.test_suite_dict = None
        
    # Parse the directories to create the test dictionary
    def Parse(self):
        ret = ERROR
        if self.dir_list != None:
            print("### Parsing...")
            for dir in self.dir_list:
                ret = self.ParseDirectory(dir)
                if ret != OK:
                    Log.Log(Log.ERROR, "Parsing " + dir)
                    break
                
        if ret == OK:
            Log.Log(Log.DEBUG, "Parse result: " + self.TestSuiteDictionaryToString())
        return ret

    # Run the test dictionary
    def Run(self):
        ret = ERROR
        if self.commands:
            print("### Running...")
            ret = self.CheckCommandsValidity()
            if ret != OK:
                Log.Log(Log.ERROR, "Commands are not valid")
                return ret
            
#             Log.Log(Log.DEBUG, "" + repr(self.commands))

            for suite in self.test_suite_dict:
                ret = self.RunSuite(self.test_suite_dict[suite]) # We continue even if it fails
                if ret != OK:
                    break
        else:
            Log.Log(Log.ERROR, "No commands to run test")
        return ret
    
    # Generate the test reports
    def GenerateReports(self):
        ret = OK
        print("### Generating reports...")
        # TODO implement
        return ret
    
    # Parse a directory to find test suite files
    def ParseDirectory(self, dir):
        ret = ERROR
        Log.Log(Log.DEBUG, "Parsing dir: " + str(dir))
        file_list = os.listdir(dir)
        Log.Log(Log.DEBUG, "File list: " + str(file_list))
        for file in file_list:
            full_file = os.path.join(dir, file)
            if os.path.isfile(full_file) and self.CheckIsTestSuiteFile(file) == OK:
#                 Log.Log(Log.DEBUG, "Found test file: " + str(file))
                ret = self.ParseFile(full_file)
                if ret != OK:
                    Log.Log(Log.WARNING, "Error while parsing " + file)
        return ret
    
    # Check commands validity
    def CheckCommandsValidity(self):
        ret = OK
        command_number = 0 # At least one is required
        for cmd in COMMAND_LIST:
            if self.commands.has_key(cmd):
                command_number = command_number + 1
                if not self.commands[cmd].has_key(COMMAND_COMMAND): # Mandatory
                    ret = ERROR
                    break
                if not self.commands[cmd].has_key(COMMAND_RESULT):
                    self.commands[cmd][COMMAND_RESULT] = COMMAND_DEFAULT_RESULT
                    Log.Log(Log.WARNING, "Forced the intermediate result file for " + cmd + " to: " + COMMAND_DEFAULT_RESULT)
        if command_number <=0:
            ret = ERROR
        return ret
    
    # Check if the file is a test suite (Ending with TestSuite.xxx)
    def CheckIsTestSuiteFile(self, file):
        file_str = str(file)
        if file_str.endswith(GTEST_EXT) or file_str.endswith(CPPUNIT_EXT) or file_str.endswith(JUNIT_EXT) or file_str.endswith(CUNIT_EXT):
            return OK 
        return ERROR
    
    # Sniff a file to detect type of test suite
    def SniffFile(self, file):
        if self.SniffGtest(file):
            return TestGlobal.GTEST_TYPE
        if self.SniffJunit(file):
            return TestGlobal.JUNIT_TYPE
        if self.SniffCppunit(file):
            return TestGlobal.CPPUNIT_TYPE
        if self.SniffCunit(file):
            return TestGlobal.CUNIT_TYPE
        
        return TestGlobal.NONE_TYPE
    
    # Sniff if it is Gtest
    def SniffGtest(self, file):
        confidence = 0
        if file.endswith(GTEST_EXT):
            f = open(file)
            content = f.read()
            f.close()
            if re.search("include.*gtest\.h", content):
                confidence = confidence + 5
            if re.search("TEST_F[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("EXPECT_EQ[ \t]*\(.*\)", content):
                confidence = confidence + 3
            if re.search("EXPECT_NE[ \t]*\(.*\)", content):
                confidence = confidence + 3
            if re.search("EXPECT_\W+[ \t]*\(.*\)", content):
                confidence = confidence + 2
            if re.search("ASSERT_\W+[ \t]*\(.*\)", content):
                confidence = confidence + 1
            if re.search("TEST[ \t]*\(.*\)", content):
                confidence = confidence + 1
            
        if confidence >= 5:
            return True
        return False
    
    # Sniff if it is Junit
    def SniffJunit(self, file):
        confidence = 0
        if file.endswith(JUNIT_EXT):
            f = open(file)
            content = f.read()
            f.close()
            if re.search("import.*org.junit.*", content):
                confidence = confidence + 5
            if re.search("assertEquals[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("assertArrayEquals[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("assertNotSame[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("assertNotNull[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("assertSame[ \t]*\(.*\)", content):
                confidence = confidence + 4
            if re.search("assertTrue[ \t]*\(.*\)", content):
                confidence = confidence + 4
            
        if confidence >= 5:
            return True
        return False
    
    # Sniff if it is Cppunit
    def SniffCppunit(self, file):
        # TODO Implement
        return False
    
    # Sniff if it is Cunit
    def SniffCunit(self, file):
        # TODO Implement
        return False
    
    # Parse a test suite file to find test framework type
    def ParseFile(self, file):
        ret = OK
        suite_type = self.SniffFile(file)
        if suite_type != None: # Just ignore the file if suite_type is None
            ret = self.ParseFileType(file, suite_type)
        return ret
    
    # Parse file of type
    def ParseFileType(self, file, type):
        Log.Log(Log.DEBUG, "Parsing " + type + " file: " + str(file))
        ret = ERROR
        ts = None
        tc = None
        suite_regexp = None
        case_regexp_list = None
        if type == TestGlobal.GTEST_TYPE:
            suite_regexp = GTEST_SUITE_REGEXP
            case_regexp_list = GTEST_CASE_REGEXP_LIST
        elif type == TestGlobal.JUNIT_TYPE:
            suite_regexp = JUNIT_SUITE_REGEXP
            case_regexp_list = JUNIT_CASE_REGEXP_LIST
            # TODO Implement other framework
        else:
            Log.Log(Log.ERROR, "Unknown file type in ParseFileType!")
            return ERROR
        
        f = open(file)
        content = f.read()
        f.close()
        
        # Parsing Suite description
        for m in re.finditer(suite_regexp, content, re.MULTILINE|re.DOTALL):
            if m != None and ts == None:
#                 Log.Log(Log.DEBUG, "Suite: " + m.group(0))
                ts = TestSuite()
                ret = ts.ParseHeader(m.group(0))
                if ret != OK:
                    break
                # Verify
                suite_name = os.path.basename(file).split('.')[0]
                if ts.suite != suite_name:
                        Log.Log(Log.WARNING, "Some suite comment inconsistencies are detected in " + os.path.basename(file) + ": " + ts.suite + " != " + suite_name)
            else:
                ret = ERROR
                break
        
        if ret != OK:
            Log.Log(Log.ERROR, "Invalid suite format in " + os.path.basename(file))
            return ret
        
        ts.type = type
        ts.test_case_dict = dict()
        
        # Parsing Case descriptions
        ret = ERROR
        for case_regexp in case_regexp_list:
            for m in re.finditer(case_regexp, content, re.MULTILINE|re.DOTALL):
                if m != None:
#                     Log.Log(Log.DEBUG, "Case: " + m.group(1))
                    tc = TestCase()
                    ret = tc.ParseHeader(m.group(1))
                    if ret == OK:
                        # Verify
                        if type == TestGlobal.GTEST_TYPE and (ts.suite != m.group(2) or tc.case !=  m.group(3)):
                            Log.Log(Log.WARNING, "Some test comment inconsistencies are detected in " + os.path.basename(file) + ": " + m.group(2) + "." + m.group(3) + " != " + ts.suite + "." + tc.case)
                        if type == TestGlobal.JUNIT_TYPE and tc.case !=  m.group(2):
                            Log.Log(Log.WARNING, "Some test comment inconsistencies are detected in " + os.path.basename(file) + ": " + m.group(2) + " != " + tc.case)
                            
                        # Add tc into ts
                        if tc.case in ts.test_case_dict:
                            Log.Log(Log.WARNING, "Test case " + tc.case + " duplicated in " + ts.suite + ". Test case ignored!")
                        else:
                            tc.suite = ts # Add a backward link to the suite as well
                            ts.test_case_dict[tc.case] = tc
                    else:
                        Log.Log(Log.WARNING, "Impossible to parse header: " + m.group(1))
                        ret = OK # Just continue
                else:
                    Log.Log(Log.WARNING, "No test cases in test suite!")
                    ret = ERROR
                    break
            
        # Add ts to class dictionary
        if not self.test_suite_dict:
            self.test_suite_dict = dict()
        if ts.suite in self.test_suite_dict:
            Log.Log(Log.WARNING, "Test suite " + ts.suite + " duplicated. Test case ignored!")
        else:
            self.test_suite_dict[ts.suite] = ts
            
        return ret
    
    # Run a single test suite
    def RunSuite(self, ts):
        Log.Log(Log.DEBUG, "Running " + ts.type + " suite: " + ts.suite)
        ret = OK
        suite_commands = None
        
        # Check if included or excluded
        # TODO Implement
        
        # Check if we have the suite commands for it
        if self.commands.has_key(ts.type):
            suite_commands = self.commands[ts.type][COMMAND_COMMAND]
            
        if not suite_commands:
            Log.Log(Log.WARNING, "Do not have command for " + ts.type + " suites.")
            return ERROR
        
        # Substitute the suite name in the command
        suite_commands = re.sub(COMMAND_SUITE, ts.suite, suite_commands)
        
        # Then run the cases    
        for case in ts.test_case_dict:
            ret = self.RunCase(ts.test_case_dict[case], suite_commands)
            if ret != OK:
                break
        return ret

    # Run a single test case
    def RunCase(self, tc, commands):
        print("Running " + tc.suite.suite + "." + tc.case)
        ret = OK
        
        # Check if included or excluded
        # TODO Implement
        
        # Substitute the case name in the command
        case_commands = re.sub(COMMAND_CASE, tc.case, commands)
        
        # Run
        ret = self.RunCommands(case_commands)
        
        return ret
    
    # Run commands for the test case
    def RunCommands(self, commands):
        ret = OK
        for cmd in commands.split(COMMAND_DELIMITER):
            Log.Log(Log.DEBUG, "Executing: " + cmd)
            args = shlex.split(cmd)
            output = ""
            try:
                output = subprocess.check_output(args)
            except subprocess.CalledProcessError as e:
                output = e.output
            except:
                ret = ERROR
            Log.Log(Log.DEBUG, "" + str(output))
        return ret, output

    # Stringnify the dictionary
    def TestSuiteDictionaryToString(self):
        s = ""
        for suite in self.test_suite_dict:
            s += self.test_suite_dict[suite].ToString()
        return s
    
