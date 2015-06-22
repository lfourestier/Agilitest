# Author Luc Fourestier (luc.fourestier@gmail.com)
#

import TestGlobal

# Constant
OK = TestGlobal.OK
ERROR = TestGlobal.ERROR

# Define a test command
class TestCommand:
    def __init__(self):
        self.type = None
        self.command_list = None
        self.result = None  # Intermediate result file

