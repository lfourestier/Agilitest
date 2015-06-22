# Author Luc Fourestier (luc.fourestier@gmail.com)
#

import re
import TestGlobal

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Define a test result for ONE case
class TestResult:
    def __init__(self):
        self.result = None  # PASS or FAIL
        self.time = None  # Date +  hour,min,sec
        self.duration = None  # The duration
        self.details = None  # Any result details
        
