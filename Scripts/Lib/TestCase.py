# Author Luc Fourestier (luc.fourestier@gmail.com)
#

import re
import TestGlobal
import Log

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Case fields
CASE_DESCRIPTION_REGEXP = "@test\s+(\w+)\s+(.*?)@\w+"
CASE_PRE_REGEXP = "@pre\s+(.*?)@\w+"
CASE_POST_REGEXP = "@post\s+(.*?)@\w+"
CASE_RESULT_REGEXP = "@result\s+(.*?)@\w+"
CASE_KEYWORDS_REGEXP = "@remarks\s+([\w, ]+)\s+"

# Define a test case
class TestCase:
    def __init__(self):
        self.case = None
        self.suite = None
        self.description = None
        self.keywords = None  # Regression, system, unit...
        self.preconditions = None
        self.postconditions = None
        self.expected = None
        self.test_case_result = None  # See TestResult

     # Parsing the Case header
    def ParseHeader(self, header):
        ret = OK
        m = re.search(CASE_DESCRIPTION_REGEXP, header, re.MULTILINE|re.DOTALL)
        if m != None:
#             Log.Log(Log.DEBUG, "case.description: " + m.group(0))
            self.case = m.group(1)
            self.description = TestGlobal.StripCommentStars(m.group(2))
            
            n = re.search(CASE_PRE_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.pre: " + n.group(0))
                self.preconditions = TestGlobal.StripCommentStars(n.group(1))
                
            n = re.search(CASE_POST_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.post: " + n.group(0))
                self.preconditions = TestGlobal.StripCommentStars(n.group(1))
                
            n = re.search(CASE_RESULT_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.expected: " + n.group(0))
                self.expected = TestGlobal.StripCommentStars(n.group(1))
                
            n = re.search(CASE_KEYWORDS_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.keywords: " + n.group(0))
                self.keywords = n.group(1)
            else:
                ret = ERROR
        else:
            ret = ERROR
        return ret
   
    def ToString(self):
        s = ""
        s += "\nTestCase: " + str(self.case)
        s += "\n\tDescription: " + str(self.description)
        s += "\n\tPre: " + str(self.preconditions)
        s += "\n\tPost: " + str(self.postconditions)
        s += "\n\tExpected: " + str(self.expected)
        s += "\n\tKeywords: " + str(self.keywords)
        return s
    
    
