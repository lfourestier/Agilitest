# Free to use
#

import TestGlobal
import Log
from TestSuite import TestSuite
from TestCase import TestCase
import TestReport

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

ALWAYS = "ALWAYS"
NO_RUN = TestReport.NO_RUN

# Define a test filter
class TestFilter:
    
    def __init__(self, include_list, exclude_list):
        self.include_list = include_list
        self.include_list.append(ALWAYS) # Will always run the tests marked as ALWAYS
        self.exclude_list = exclude_list
        self.include_list.append(NO_RUN) # Will always exclude the tests marked as NO_RUN

    # Check if it is filtered out based on the keywords, suite name (Return Bool)
    def IsSuiteFiltered(self, suite):
        ret = False
        keyword_list = suite.keywords.split(',')
        if not keyword_list:
            keyword_list.append(ALWAYS) # No keywords means no filtering
        keyword_list.append(suite.suite)
        
        for key in keyword_list:
            if key in self.include_list and key not in self.exclude_list:
                ret = True
        return ret
    
    # Check if it is filtered out based on the keywords, case name (Return Bool)
    def IsCaseFiltered(self, case):
        ret = False
        keyword_list = case.keywords.split(',')
        keyword_list.append(case.suite.suite + "." + case.case)
        return ret