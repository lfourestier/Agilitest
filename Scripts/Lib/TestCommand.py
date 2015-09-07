# Free to use
#

import subprocess
import shlex
import TestGlobal
import Log
import re
import os
from TestResult import TestResult

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Commands
COMMAND_LIST = [TestGlobal.GTEST_TYPE, TestGlobal.JUNIT_TYPE, TestGlobal.CPPUNIT_TYPE, TestGlobal.CUNIT_TYPE]
COMMAND_COMMAND = "command"
COMMAND_RESULT = "result"
COMMAND_DEFAULT_RESULT = "Result.xml"
COMMAND_DELIMITER = "@@"
COMMAND_SUITE_MACRO = "@SUITE"
COMMAND_CASE_MACRO = "@CASE"
COMMAND_RESULT_MACRO = "@RESULT"
COMMAND_FILE_PATH_MACRO ="@PWD"

# Define a test command
class TestCommand:
    def __init__(self, commands, command_path):
        self.commands = commands
        self.command_path = command_path
        self.output = None

    # Check commands validity
    def CheckValidity(self):
        ret = OK
        if not self.commands:
            Log.Log(Log.ERROR, "No commands to run test")
            return ERROR
        command_number = 0 # At least one is required
        for cmd in COMMAND_LIST:
            if self.commands.has_key(cmd):
                command_number = command_number + 1
                if not self.commands[cmd].has_key(COMMAND_COMMAND): # Mandatory
                    Log.Log(Log.ERROR, "Commands are not valid")
                    ret = ERROR
                    break
#                 if not self.commands[cmd].has_key(COMMAND_RESULT):
#                     self.commands[cmd][COMMAND_RESULT] = COMMAND_DEFAULT_RESULT
#                     Log.Log(Log.WARNING, "Forced the intermediate result file for " + cmd + " to: " + COMMAND_DEFAULT_RESULT)
        if command_number <=0:
            ret = ERROR
        return ret
    
    # Execute a test
    def ExecuteTest(self, tc):
        # Check if we have the commands for the suite type
        if self.commands.has_key(tc.suite.type):
            commands = self.commands[tc.suite.type][COMMAND_COMMAND]
            
        if not commands:
            Log.Log(Log.WARNING, "Do not have command for " + tc.suite.type + " suites.")
            return ERROR
        
        # get intermediate result file location
        result = None
        if self.commands[tc.suite.type].has_key(COMMAND_RESULT):
            result = self.commands[tc.suite.type][COMMAND_RESULT]
        
        # Substitute the macros in the command
        commands = re.sub(COMMAND_SUITE_MACRO, tc.suite.suite, commands)
        commands = re.sub(COMMAND_CASE_MACRO, tc.case, commands)
        if result:
            commands = re.sub(COMMAND_RESULT_MACRO, result, commands)
        else:
            commands = re.sub(COMMAND_RESULT_MACRO, "", commands)
        if self.command_path:
            commands = re.sub(COMMAND_FILE_PATH_MACRO, self.command_path, commands)
        else:
            commands = re.sub(COMMAND_FILE_PATH_MACRO, "", commands)
            
        # Process
        ret = self.ProcessCommands(commands)
        if ret != OK:
            Log.Log(Log.DEBUG, "Error while processing commands")
            return ret
        
        # Parse output
        tr = TestResult(tc.suite.type)
        if self.output:
            ret = tr.ParseOutput(self.output)
            if tr.suite_name == "Unknown":
                tr.suite_name = tc.suite.suite
            if tr.case_name == "Unknown":
                tr.case_name = tc.case
            if tr.suite_name != tc.suite.suite or tr.case_name != tc.case:
                Log.Log(Log.WARNING, "Test result looks incoherent compared to test case run. " + tr.suite_name + "!=" + tc.suite.suite + " or " + tr.case_name + "!=" + tc.case)
            if ret != OK:
                return ret
        else:
            Log.Log(Log.WARNING, "No output to parse")
            ret = ERROR

        # Parse intermediate result
        if result:
            try:
                f = open(result)
            except:
                f = None
            if not f:
                Log.Log(Log.WARNING, "Cannot open result file.")
                ret = ERROR
            else:
                content = f.read()
                if not content:
                    Log.Log(Log.WARNING, "Intermediate result file is empty!")
                    ret = ERROR
                f.close()
                os.remove(result)
            if ret == OK:
                ret = tr.ParseResult(content)
                if ret != OK:
                    return ret
            
        # Add tr into tc
        if ret == OK:
            tc.test_case_result = tr
        else:
            ret = OK # We continue anyway
        return ret
    
    # Execute the commands in a process
    def ProcessCommands(self, commands):
        ret = OK
        self.output = ""
        for cmd in commands.split(COMMAND_DELIMITER):
            Log.Log(Log.DEBUG, "Executing: " + cmd)
            args = shlex.split(cmd)
            try:
                self.output += subprocess.check_output(args, shell=True)
            except subprocess.CalledProcessError as e:
                self.output += '\n' + e.output
                break
            except Exception as e:
                Log.Log(Log.ERROR, "Unexpected error while executing command: " + str(e))
                ret = ERROR
                break
#             self.output += '\n'
        return ret

