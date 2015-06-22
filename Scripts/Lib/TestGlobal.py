# Author Luc Fourestier (luc.fourestier@gmail.com)
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
    str = re.sub(" \* ", " ", str)
    str = re.sub("\* ", " ", str)
    str = re.sub(" \*", " ", str)
    return str

# Strip string from white spaces
def StripWhiteSpaces(str):
    str = re.sub("\S", "", str)
    return str


