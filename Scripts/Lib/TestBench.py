# Free to use
#

import os
import os.path
import re
import subprocess
import shlex

import Log
import TestGlobal
from TestSuite import TestSuite
from TestCase import TestCase
from TestResult import TestResult
from TestReport import TestReport
from TestCommand import TestCommand

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
COMMAND_SUITE_MACRO = "@SUITE"
COMMAND_CASE_MACRO = "@CASE"
COMMAND_RESULT_MACRO = "@RESULT"

# Reg Exp

GTEST_SUITE_REGEXP = "(@defgroup.*?)@\{"
GTEST_CASE_REGEXP_LIST = ["/\*\*[\s\*]+(@test.*?)\*/\s+.*?TEST_F\(\w+\s*,\s*(\w+)\)"] #, "(@test.*?)TEST\((\w+)\s*,\s*(\w+)\)"]

JUNIT_SUITE_REGEXP = "(@defgroup.*?)@\{"
JUNIT_CASE_REGEXP_LIST = ["/\*\*[\s\*]+(@test.*?)\*/\s+.*?@Test.*?(test\w+)\s*\("]

# The test bench class that provides test management functions
class TestBench:
    def __init__(self, dir_list, commands, report_file, synthesis_file):
        self.dir_list = dir_list  # As list
        self.test_command = TestCommand(commands)  # As dictionary {gtest:blabla, junit:sdfsdf, ...}
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
            Log.Log(Log.DEBUG, "Parsing results: " + self.TestSuiteDictionaryToString())
        return ret

    # Run the test dictionary
    def Run(self):
        print("### Running...")
        ret = self.test_command.CheckValidity()
        if ret != OK:
            Log.Log(Log.ERROR, "Commands are not valid")
            return ret
        
        if not self.test_suite_dict:
            Log.Log(Log.ERROR, "No element in test dictionary")
            return ERROR
        
        for suite in self.test_suite_dict:
            ret = self.RunSuite(self.test_suite_dict[suite]) # We continue even if it fails
            if ret != OK:
                Log.Log(Log.ERROR, "Run error!")
                break
            
        if ret == OK:
            Log.Log(Log.DEBUG, "Running results: " + self.TestSuiteDictionaryToString())
        return ret
    
    # Generate the test reports
    def GenerateReports(self):
        ret = OK
        print("### Generating reports...")
        tr = TestReport(self.test_suite_dict)
        if self.report_file and self.report_file.endswith(".csv"):
            print("Test report: " + self.report_file)
            ret = tr.CreateCsvReport(self.report_file)
        if ret != OK:
            return ret
        print("OK")   
        if self.synthesis_file:
            print("Test synthesis: " + self.synthesis_file)
            ret = tr.UpdateSynthesisReport(self.synthesis_file) 
        if ret == OK:
            print("OK")   
        return ret
    
    # Parse a directory to find test suite files
    def ParseDirectory(self, dir):
        ret = ERROR
        Log.Log(Log.DEBUG, "Parsing dir: " + str(dir))
        try:
            file_list = os.listdir(dir)
        except:
            return ERROR
        Log.Log(Log.DEBUG, "File list: " + str(file_list))
        for file_name in file_list:
            full_file_name = os.path.join(dir, file_name)
            if os.path.isfile(full_file_name) and self.CheckIsTestSuiteFile(file_name) == OK:
#                 Log.Log(Log.DEBUG, "Found test file_name: " + str(file_name))
                ret = self.ParseFile(full_file_name)
                if ret != OK:
                    Log.Log(Log.WARNING, "Error while parsing " + file_name)
        return ret
    
    # Check if the file is a test suite (Ending with TestSuite.xxx)
    def CheckIsTestSuiteFile(self, file_content):
        file_str = str(file_content)
        if file_str.endswith(GTEST_EXT) or file_str.endswith(CPPUNIT_EXT) or file_str.endswith(JUNIT_EXT) or file_str.endswith(CUNIT_EXT):
            return OK 
        return ERROR
    
    # Sniff a file to detect type of test suite
    def SniffFile(self, file_name):
        if self.SniffGtest(file_name):
            return TestGlobal.GTEST_TYPE
        if self.SniffJunit(file_name):
            return TestGlobal.JUNIT_TYPE
        if self.SniffCppunit(file_name):
            return TestGlobal.CPPUNIT_TYPE
        if self.SniffCunit(file_name):
            return TestGlobal.CUNIT_TYPE
        
        return TestGlobal.NONE_TYPE
    
    # Sniff if it is Gtest
    def SniffGtest(self, file_name):
        confidence = 0
        if file_name.endswith(GTEST_EXT):
            f = open(file_name)
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
    def SniffJunit(self, file_name):
        confidence = 0
        if file_name.endswith(JUNIT_EXT):
            f = open(file_name)
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
    def SniffCppunit(self, file_name):
        # TODO Implement
        return False
    
    # Sniff if it is Cunit
    def SniffCunit(self, file_name):
        # TODO Implement
        return False
    
    # Parse a test suite file to find test framework type
    def ParseFile(self, file_name):
        ret = OK
        suite_type = self.SniffFile(file_name)
        if suite_type != None: # Just ignore the file_name if suite_type is None
            ret = self.ParseFileType(file_name, suite_type)
        return ret
    
    # Parse file of type
    def ParseFileType(self, file_name, file_type):
        Log.Log(Log.DEBUG, "Parsing " + file_type + " file: ")
        print(str(file_name))
        ret = ERROR
        ts = None
        tc = None
        suite_regexp = None
        case_regexp_list = None
        if file_type == TestGlobal.GTEST_TYPE:
            suite_regexp = GTEST_SUITE_REGEXP
            case_regexp_list = GTEST_CASE_REGEXP_LIST
        elif file_type == TestGlobal.JUNIT_TYPE:
            suite_regexp = JUNIT_SUITE_REGEXP
            case_regexp_list = JUNIT_CASE_REGEXP_LIST
            # TODO Implement other framework
        else:
            Log.Log(Log.ERROR, "Unknown file type in ParseFileType!")
            return ERROR
        
        f = open(file_name)
        content = f.read()
        f.close()
        
        # Parsing Suite description
        for m in re.finditer(suite_regexp, content, re.MULTILINE|re.DOTALL):
            if m != None and ts == None:
                ts = TestSuite()
#                 Log.Log(Log.DEBUG, "Suite: " + TestGlobal.StripCommentStars(m.group(1)))
                ret = ts.ParseHeader(TestGlobal.StripCommentStars(m.group(1)))
                if ret != OK:
                    break
                # Verify
                suite_name = os.path.basename(file_name).split('.')[0]
                if ts.suite != suite_name:
                        Log.Log(Log.WARNING, "Some suite comment inconsistencies are detected in " + os.path.basename(file_name) + ": " + ts.suite + " != " + suite_name)
            else:
                ret = ERROR
                break
        
        if ret != OK:
            Log.Log(Log.ERROR, "Invalid suite format in " + os.path.basename(file_name))
            return ret
        
        ts.type = file_type
        ts.test_case_dict = dict()
        
        # Parsing Case descriptions
        ret = ERROR
        for case_regexp in case_regexp_list:
            for m in re.finditer(case_regexp, content, re.MULTILINE|re.DOTALL):
                if m != None:
                    tc = TestCase()
                    tc.suite = ts # Add a backward link to the suite as well
                    tc.case =  m.group(2)
#                     Log.Log(Log.DEBUG, "Case: " + TestGlobal.StripCommentStars(m.group(1)))
                    ret = tc.ParseHeader(TestGlobal.StripCommentStars(m.group(1)))
                    if ret == OK:
                        # Add tc into ts
                        if tc.case in ts.test_case_dict:
                            Log.Log(Log.WARNING, "Test case " + tc.case + " duplicated in " + ts.suite + ". Test case ignored!")
                        else:
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
            
        if ret == OK:
            print("OK")
        else:
            print("ERROR")
            
        return ret
    
    # Run a single test suite
    def RunSuite(self, ts):
        Log.Log(Log.DEBUG, "Running " + ts.type + " suite: " + ts.suite)
        ret = OK
        
        # Check if included or excluded
        # TODO Implement
        
        # Then run the cases    
        for case in ts.test_case_dict:
            ret = self.RunCase(ts.test_case_dict[case])
            if ret != OK:
                break
        return ret

    # Run a single test case
    def RunCase(self, tc):
        print(tc.suite.suite + "." + tc.case)
        
        # Check if included or excluded
        # TODO Implement
        
        # Execute
        ret = self.test_command.ExecuteTest(tc)
        if ret != OK:
            return ret
        
        if tc.test_case_result:
            if tc.test_case_result.status == TestResult.FAIL:
                print tc.test_case_result.details
            print(tc.test_case_result.status)
        else:
            print("FAIL")
                
        return ret
    
    # Stringnify the dictionary
    def TestSuiteDictionaryToString(self):
        s = ""
        for suite in self.test_suite_dict:
            s += self.test_suite_dict[suite].ToString()
        return s
    