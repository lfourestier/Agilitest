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


# Pass or fail
PASS = "PASS"
FAIL = "FAIL"


# Define a test status for ONE case
class TestResult:
    def __init__(self, type):
        self.status = FAIL  # PASS or FAIL
        self.type = type # Type of suite
        self.time = None  # Date +  hour,min,sec
        self.duration = None  # The duration
        self.details = None  # Any status details
        self.output = None
        self.result = None
        
    def ParseOutput(self, output):
        ret = OK
        self.output = output
        if self.type == TestGlobal.GTEST_TYPE:
            m = re.search(OUTPUT_PASS_GTEST, output)
            if m and int(m.group(1)) > 0:
                self.status = PASS
            m = re.search(OUTPUT_FAIL_GTEST, output)
            if m and int(m.group(1)) > 0:
                self.status = FAIL
        elif self.type == TestGlobal.JUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Junit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CPPUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Cppunit ParseOutput not yet implemented")
        elif self.type == TestGlobal.CUNIT_TYPE:
            Log.Log(Log.VERBOSE, "TODO Cunit ParseOutput not yet implemented")
        else:
            ret = ERROR
            
        return ret
        
    def ParseResult(self, result):
        ret = OK
        self.result = result
        Log.Log(Log.DEBUG, result)
        return ret
            
            