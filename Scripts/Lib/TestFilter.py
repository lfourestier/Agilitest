# Free to use
#

import TestGlobal
import Log
from TestSuite import TestSuite
from TestCase import TestCase
from __builtin__ import True

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR


# Define a test filter
class TestFilter:
    ALWAYS = "ALWAYS"
    NO_RUN = "NEVER"
    
    def __init__(self, include_list, exclude_list):
        self.include_list = include_list
        self.exclude_list = exclude_list

    # Check if it is filtered out based on the keywords, suite name (Return True if to be run )
    def IsSuiteIncluded(self, suite):
        ret = False
        # Get keywords
        keyword_list = None
        if suite.keywords:
            keyword_list = suite.keywords.split(',')
        if not keyword_list:
            keyword_list = list()
            keyword_list.append(self.ALWAYS) # No keywords means no filtering, so append ALWAYS
        keyword_list.append(suite.suite)
        # Filter 
        included = False
        excluded = False
        for key in keyword_list:
            if not self.include_list or key in self.include_list or key == self.ALWAYS:
                Log.Log(Log.VERBOSE, key + " is included")
                included = True
            if (self.exclude_list and key in self.exclude_list) or key == self.NO_RUN:
                Log.Log(Log.VERBOSE, key + " is excluded")
                excluded = True
        if included and not excluded:
            ret = True
        Log.Log(Log.DEBUG, "Suite " + suite.suite + " included: " + str(ret))
        return ret
    
    # Check if it is filtered out based on the keywords, case name (Return  True if to be run )
    def IsCaseIncluded(self, case):
        ret = False
        # Get keywords
        keyword_list = None
        if case.keywords:
            keyword_list = case.keywords.split(',')
        if case.suite.keywords:
            keyword_list.extend(case.suite.keywords.split(',')) # The cases inherits from the Suite keywords
        if not keyword_list:
            keyword_list = list()
            keyword_list.append(self.ALWAYS) # No keywords means no filtering, so append ALWAYS
        keyword_list.append(case.case)
        keyword_list.append(case.suite.suite + "." + case.case)
        # Filter 
        included = False
        excluded = False
        for key in keyword_list:
            if not self.include_list or key in self.include_list or key == self.ALWAYS:
                Log.Log(Log.VERBOSE, key + " is included")
                included = True
            if (self.exclude_list and key in self.exclude_list) or key == self.NO_RUN: 
                Log.Log(Log.VERBOSE, key + " is excluded")
                excluded = True
        if included and not excluded:
            ret = True
        Log.Log(Log.DEBUG, "Case " + case.case + " included: " + str(ret))
        return ret
     