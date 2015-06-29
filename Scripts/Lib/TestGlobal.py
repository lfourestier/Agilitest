# Free to use
#

import re

# Constant
OK = 0
ERROR = -1

# Supported test framework/suite types
GTEST_TYPE = "Gtest"
JUNIT_TYPE = "Junit"
CPPUNIT_TYPE = "Cppunit"
CUNIT_TYPE = "Cunit"

NONE_TYPE = "None" # When unknown framework


# Strip string from comment stars
def StripCommentStars(str):
    str = re.sub("\n[\s\*]+", " ", str)
    return str

# Strip string from white spaces
def StripWhiteSpaces(str):
    str = re.sub("[ \t]+", "", str)
    return str

# Strip string from white spaces
def StripCarriageReturn(str):
    str = re.sub("[\r\n]+", " ", str)
    return str


