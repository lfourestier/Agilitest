# Free to use
#

import re
import TestGlobal
import Log

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Case fields
CASE_DESCRIPTION_REGEXP = "@test\s+(.*?)@\w+"
CASE_PRE_REGEXP = "@pre\s+(.*?)@\w+"
CASE_POST_REGEXP = "@post\s+(.*?)@\w+"
CASE_RESULT_REGEXP = "@result\s+(.*?)@\w+"
CASE_KEYWORDS_REGEXP = "@remarks\s+([\w, ]+)\s+@\w+"
CASE_PRIORITY_REGEXP = "@priority\s+(.*?)@\w+"

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
        self.priority = None
        self.test_case_result = None  # See TestResult

    # Parsing the Case header
    def ParseHeader(self, header):
        ret = OK
        header += " @stop" # Required to stop the search
        m = re.search(CASE_DESCRIPTION_REGEXP, header, re.MULTILINE|re.DOTALL)
        if m != None:
#             Log.Log(Log.DEBUG, "case.description: " + m.group(0))
            self.description = m.group(1)
            
            n = re.search(CASE_PRE_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.pre: " + n.group(0))
                self.preconditions = n.group(1)
                
            n = re.search(CASE_POST_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.post: " + n.group(0))
                self.postconditions = n.group(1)
                
            n = re.search(CASE_RESULT_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.expected: " + n.group(0))
                self.expected = n.group(1)
                
            n = re.search(CASE_KEYWORDS_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.keywords: " + n.group(0))
                self.keywords = TestGlobal.StripWhiteSpaces(n.group(1))
            else:
                Log.Log(Log.WARNING, "Missing keywords for " + self.suite.suite + "." + self.case + ". Test will be ignored while running!")
                    
                
            n = re.search(CASE_PRIORITY_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "case.keywords: " + n.group(0))
                self.priority = n.group(1)
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
        s += "\n\tPriority: " + str(self.priority)
        if self.test_case_result:
            s += self.test_case_result.ToString()
        return s
    
    
