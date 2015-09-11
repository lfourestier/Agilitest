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
class TestRules:
    ALWAYS = "ALWAYS"
    NO_RUN = "NO_RUN"
    FIRST = "FIRST"
    LAST = "LAST"
    EXCLUDE = "EXCLUDE"
    IGNORE = "IGNORE"
    
    def __init__(self, include_list, exclude_list):
        self.include_list = include_list
        self.exclude_list = exclude_list

    # Check if it is filtered out based on the keywords and meta information, suite name (Return True if to be run )
    def IsSuiteIncluded(self, suite):
        ret = False
        included = False
        excluded = False
        # Get meta information
        meta_info_list = None 
        if suite.meta:
            meta_info_list = suite.meta.split(',')
        # Get keywords
        keyword_list = None
        if suite.keywords:
            keyword_list = suite.keywords.split(',')
        if not keyword_list:
            keyword_list = list()
            keyword_list.append(self.ALWAYS) # No keywords means no filtering, so append ALWAYS
        keyword_list.append(suite.suite)
        # Filter 
        if meta_info_list:
            if self.EXCLUDE in meta_info_list or self.IGNORE in meta_info_list:
                excluded = True
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
    
    # Check if it is filtered out based on the keywords and meta information, case name (Return  True if to be run )
    def IsCaseIncluded(self, case):
        ret = False
        included = False
        excluded = False
        # Get meta information
        meta_info_list = None
        if case.meta:
            meta_info_list = case.meta.split(',')
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
        if meta_info_list:
            if self.EXCLUDE in meta_info_list or self.IGNORE in meta_info_list:
                excluded = True
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

    # Check if the suite has to be ignored according to the meta information
    def IsSuiteIgnored(self, suite):
        ret = False
        ignored = False
        # Get meta information
        meta_info_list = None 
        if suite.meta:
            meta_info_list = suite.meta.split(',')
        # Filter 
        if meta_info_list:
            if self.IGNORE in meta_info_list:
                ignored = True
        if ignored:
            ret = True
        Log.Log(Log.DEBUG, "Suite " + suite.suite + " ignored: " + str(ret))
        return ret
    
    # Check if the case has to be ignored according to the meta information
    def IsCaseIgnored(self, case):
        ret = False
        ignored = False
        # Get meta information
        meta_info_list = None 
        if case.meta:
            meta_info_list = case.meta.split(',')
        # Filter 
        if meta_info_list:
            if self.IGNORE in meta_info_list:
                ignored = True
        if ignored:
            ret = True
        Log.Log(Log.DEBUG, "Case " + case.case + " ignored: " + str(ret))
        return ret
    
    # get the first test case to run
    def GetFirstCase (self, suite):
        ret = None
        for case in suite.test_case_dict:
            meta_info_list = None 
            if suite.test_case_dict[case].meta:
                meta_info_list = suite.test_case_dict[case].meta.split(',')
            if meta_info_list and self.FIRST in meta_info_list:
                ret = suite.test_case_dict[case]
                break
        return ret
    
    # get the last test case to run
    def GetLastCase (self, suite):
        ret = None
        for case in suite.test_case_dict:
            meta_info_list = None 
            if suite.test_case_dict[case].meta:
                meta_info_list = suite.test_case_dict[case].meta.split(',')
            if meta_info_list and self.LAST in meta_info_list:
                ret = suite.test_case_dict[case]
                break
        return ret

    # Check if test is not first and not last
    def IsCaseNotFirstAndNotLast(self, case):
        ret = True
        if case.meta:
            meta_info_list = case.meta.split(',')
            if meta_info_list and (self.FIRST in meta_info_list or self.LAST in meta_info_list):
                ret = False
        return ret
                
