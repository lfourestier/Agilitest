# Author Luc Fourestier (luc.fourestier@gmail.com)
#

import re
import TestGlobal
import Log

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# output
OUTPUT_PASS_GTEST = "\[\s+PASSED\s+\]\s+(\d+)\s+test"
OUTPUT_FAIL_GTEST = "\[\s+FAILED\s+\]\s+(\d+)\s+test"

# result
RESULT_XML_FORMAT = "<?xml version=\""


# Define a test status for ONE case
class TestResult:
    PASS = "PASS"
    FAIL = "FAIL"
    
    def __init__(self, type):
        self.status = self.FAIL  # PASS or FAIL
        self.type = type # Type of suite
        self.time = None  # Date +  hour,min,sec
        self.duration = None  # The duration
        self.details = "No details"  # Any status details
        self.output = None
        self.result = None
        
    # Parse process output
    def ParseOutput(self, output):
        ret = OK
        self.output = output
        if self.type == TestGlobal.GTEST_TYPE:
            m = re.search(OUTPUT_PASS_GTEST, output)
            if m and int(m.group(1)) > 0:
                self.status = self.PASS
            m = re.search(OUTPUT_FAIL_GTEST, output)
            if m and int(m.group(1)) > 0:
                self.status = self.FAIL
        elif self.type == TestGlobal.JUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Junit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CPPUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Cppunit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Cunit ParseOutput not yet implemented")
        else:
            ret = ERROR
            
        return ret
    
    # Parse result    
    def ParseResult(self, result):
        ret = OK
        self.result = result
        
        if self.SniffResult() == TestGlobal.JUNIT_TYPE:
            Log.Log(Log.DEBUG, "Result is Junit type.")
        Log.Log(Log.DEBUG, result)
        return ret
    
    # sniff result type
    def SniffResult(self):
        if self.SniffJunitResult(self.result):
            return TestGlobal.JUNIT_TYPE
        return TestGlobal.NONE_TYPE

    # Sniff if it is Junit result type
    def SniffJunitResult(self, result):
        confidence = 0
        if result.startswith(RESULT_XML_FORMAT):
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
        
            