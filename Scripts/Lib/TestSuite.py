# Free to use
#

import re
import TestGlobal
import Log

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Suite fields
SUITE_DESCRIPTION_REGEXP = "@defgroup\s+(\w+)\s+(\w+)\s+(.*?)@\w+"
SUITE_KEYWORDS_REGEXP = "@remarks\s+([\w, ]+)\s.*?@\w+"

# Define a test suite
class TestSuite:
    def __init__(self):
        self.suite = None
        self.description = None
        self.type = None  # Cppunit, Gtest
        self.keywords = None
        self.test_case_dict = None  # Test case dictionary (See TestCase)

    # Parsing the Suite header
    def ParseHeader(self, header):
        ret = OK
        header += " @stop" # Required to stop the search
        m = re.search(SUITE_DESCRIPTION_REGEXP, header, re.MULTILINE|re.DOTALL)
        if m != None:
#             Log.Log(Log.DEBUG, "Suite.description: " + m.group(0))
            self.suite = m.group(2)
            self.description = TestGlobal.StripCommentStars(m.group(3))
            n = re.search(SUITE_KEYWORDS_REGEXP, header, re.MULTILINE|re.DOTALL)
            if n != None:
#                 Log.Log(Log.DEBUG, "Suite.keywords: " + n.group(0))
                self.keywords = TestGlobal.StripWhiteSpaces(n.group(1))
            else:
                ret = ERROR
        else:
            ret = ERROR
        return ret
    
    def ToString(self):
        s = ""
        s += "\nTestSuite: " + str(self.suite)
        s += "\n\tDescription: " + str(self.description)
        s += "\n\tType: " + str(self.type)
        s += "\n\tKeywords: " + str(self.keywords)
        for case in self.test_case_dict:
            s += self.test_case_dict[case].ToString()
        return s
    
