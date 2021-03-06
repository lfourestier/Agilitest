# Free to use
#

import re
import TestGlobal
import Log
import xml.etree.ElementTree as ET

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# output
GTEST_OUTPUT_DETAILS = "\[\s+RUN\s+\]\s+(\w+)\.(\w+)(.*?)\[\s+(\w+)\s+\][\s\w\.]+\s+\((\d+)\sms\)"
GTEST_PASS = "OK"
GTEST_FAIL = "FAILED"

CUNIT_OUTPUT_DETAILS = "Suite\:\s+(\w+)\s+Test\:\s+(\w+)\s*\.\.\.(\w+)(.*?)Run Summary\:.*?Elapsed\s+time\s+\=\s+([\.\d]+)\s+seconds"
CUNIT_PASS = "passed"
CUNIT_FAIL = "FAILED"

PYTEST_OUTPUT_DETAILS = "collected\s+\d+\s+items\s+.*?\/(\w+)\.py\s+(.*?)[\=]+\s+\d+\s+(\w+)\s+in\s+([\.\d]+)\s+seconds\s+[\=]+"
PYTEST_PASS = "passed"
PYTEST_FAIL = "failed"

# result
XML_RESULT_FORMAT_MARKER = "<?xml version=\""

JUNIT_XML_ROOT_TAG = "testsuites"
JUNIT_XML_SUITE_TAG = "testsuite"
JUNIT_XML_CASE_TAG = "testcase"
JUNIT_XML_FAIL_TAG = "failure"
JUNIT_XML_TIMESTAMP_ATTRIB = "timestamp"
JUNIT_XML_NAME_ATTRIB = "name"
JUNIT_XML_CLASSNAME_ATTRIB = "classname"
JUNIT_XML_TIME_ATTRIB = "time"
JUNIT_XML_MSG_ATTRIB = "message"


# Define a test status for ONE case
class TestResult:
    PASS = "PASS"
    FAIL = "FAIL"
    NO_RUN = "NO_RUN"
    
    def __init__(self, suite_type):
        self.status = self.PASS  # PASS or FAIL
        self.type = suite_type # Type of suite
        self.suite_name = "Unknown"
        self.case_name = "Unknown"
        self.timestamp = "Unknown"  # Date +  hour,min,sec
        self.duration = "Unknown"  # The duration
        self.details = "No details"  # Any status details
        self.output = None
        self.result = None
        
    # Parse process output
    def ParseOutput(self, output):
        ret = OK
        self.output = output
        Log.Log(Log.DEBUG, "Parsing ouput...")
        Log.Log(Log.DEBUG, output)
        if self.type == TestGlobal.GTEST_TYPE:
            self.ParseGtestOutput(output)
        elif self.type == TestGlobal.JUNIT_TYPE:
            Log.Log(Log.DEBUG, "TODO Junit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CPPUNIT_TYPE:
            Log.Log(Log.DEBUG, "TODO Cppunit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CUNIT_TYPE:
            self.ParseCunitOutput(output)
        elif self.type == TestGlobal.PYTEST_TYPE:
            self.ParsePytestOutput(output)
        else:
            ret = ERROR
            
        return ret
    
    # Parse Gtest output
    def ParseGtestOutput(self, output):
        ret = OK
        m = re.search(GTEST_OUTPUT_DETAILS, output, re.DOTALL)
        if m:
            self.suite_name = m.group(1)
            self.case_name = m.group(2)
            self.details = TestGlobal.StripCarriageReturn(m.group(3))
            if m.group(4) == GTEST_PASS:
                self.status = self.PASS
            else:
                self.status = self.FAIL
            self.duration = str(float(m.group(5))/1000) # to seconds
            Log.Log(Log.DEBUG, "Found Gtest output details: " + self.suite_name + ", " + self.case_name+ ", " + self.details + ", " + self.status + ", " + self.duration)
        else:
            Log.Log(Log.WARNING, "Not able to parse Gtest output.")
        return ret
    
    # Parse Cunit output
    def ParseCunitOutput(self, output):
        ret = OK
        m = re.search(CUNIT_OUTPUT_DETAILS, output, re.DOTALL)
        if m:
            self.suite_name = m.group(1)
            self.case_name = m.group(2)
            self.details = TestGlobal.StripCarriageReturn(m.group(4))
            if m.group(3) == CUNIT_PASS:
                self.status = self.PASS
            else:
                self.status = self.FAIL
            self.duration = m.group(5)
            Log.Log(Log.DEBUG, "Found Cunit output details: " + self.suite_name + ", " + self.case_name + ", " + self.details + ", " + self.status + ", " + self.duration)
        else:
            Log.Log(Log.WARNING, "Not able to parse Cunit output.")
            
        return ret
    
    # Parse Pytest output
    def ParsePytestOutput(self, output):
        ret = OK
        m = re.search(PYTEST_OUTPUT_DETAILS, output, re.DOTALL)
        if m:
            self.suite_name = m.group(1)
#             self.case_name = m.group(2)
            self.details = TestGlobal.StripCarriageReturn(m.group(2))
            if m.group(3) == PYTEST_PASS:
                self.status = self.PASS
            else:
                self.status = self.FAIL
            self.duration = m.group(4)
            Log.Log(Log.DEBUG, "Found Pytest output details: " + self.suite_name + ", " + self.case_name + ", " + self.details + ", " + self.status + ", " + self.duration)
        else:
            Log.Log(Log.WARNING, "Not able to parse Pytest output.")
            
        return ret
    
    # Parse result    
    def ParseResult(self, result):
        ret = OK
        self.result = result
        Log.Log(Log.DEBUG, "Parsing result...")
        
        if self.SniffResult(result) == TestGlobal.JUNIT_TYPE:
            Log.Log(Log.DEBUG, "Result is Junit type.")
            ret = self.ParseJunitResult(result)
            
        Log.Log(Log.DEBUG, result)
        return ret
    
    # Parse Junit type result
    def ParseJunitResult(self, result):
        ret = OK
        root = ET.fromstring(result)
        if root.tag == JUNIT_XML_ROOT_TAG:
            if root.attrib.has_key(JUNIT_XML_TIMESTAMP_ATTRIB):
                self.timestamp = root.attrib[JUNIT_XML_TIMESTAMP_ATTRIB]
            suite_list = root.findall(JUNIT_XML_SUITE_TAG)
            if not suite_list:
                Log.Log(Log.ERROR, "No testsuite tag in Junit xml result")
                return ERROR
            if len(suite_list) > 1:
                Log.Log(Log.WARNING, "More than one suite detected in test result. Take the first one!")
        elif root.tag == JUNIT_XML_SUITE_TAG:
            suite_list = [root]
        else:
            Log.Log(Log.ERROR, "No testsuite tag in Junit xml result")
            return ERROR
   
        case_list =  suite_list[0].findall(JUNIT_XML_CASE_TAG)
        if not case_list:
            Log.Log(Log.ERROR, "No testcase tag in Junit xml result")
            return ERROR
        if len(case_list) > 1:
            Log.Log(Log.WARNING, "More than one case detected in test result. Take the first one!")
        if case_list[0].attrib.has_key(JUNIT_XML_CLASSNAME_ATTRIB):
            self.suite_name = case_list[0].attrib[JUNIT_XML_CLASSNAME_ATTRIB]  
        if case_list[0].attrib.has_key(JUNIT_XML_NAME_ATTRIB):
            self.case_name = case_list[0].attrib[JUNIT_XML_NAME_ATTRIB]  
        if case_list[0].attrib.has_key(JUNIT_XML_TIME_ATTRIB):
            self.duration = case_list[0].attrib[JUNIT_XML_TIME_ATTRIB] 
             
        failure_list =  case_list[0].findall(JUNIT_XML_FAIL_TAG)
        status = self.PASS
        if failure_list: 
            status = self.FAIL
            self.details = TestGlobal.StripCarriageReturn(failure_list[0].attrib[JUNIT_XML_MSG_ATTRIB])      
        if self.output:
            if self.status == self.PASS and status == self.PASS:
                self.status = self.PASS
                self.details = ""
            else:
                self.status = self.FAIL
        else:
            self.status = status
        return ret
    
    # sniff result type
    def SniffResult(self, result):
        if self.SniffJunitResult(result):
            return TestGlobal.JUNIT_TYPE
        return TestGlobal.NONE_TYPE

    # Sniff if it is Junit result type
    def SniffJunitResult(self, result):
        confidence = 0
        if result.startswith(XML_RESULT_FORMAT_MARKER):
            confidence = confidence + 1
        if re.search("\<testsuites", result):
            confidence = confidence + 2
        if re.search("\<testsuite", result):
            confidence = confidence + 2
        if re.search("\<testcase", result):
            confidence = confidence + 2
        if re.search("\<failure", result):
            confidence = confidence + 1
            
        if confidence >= 5:
            return True
        return False
        
    def ToString(self):
        s = ""
        s += "\nTestResult: " # + str(self.suite_name) + "." + str(self.case_name)
        s += "\n\tStatus: " + str(self.status)
        s += "\n\tTimestamp: " + str(self.timestamp)
        s += "\n\tDuration: " + str(self.duration)
        s += "\n\tDetails: " + str(self.details)
        return s
            