## @file OperationsPyTestSuite.py
#  @author John Doe
#  @date 2013
#  @copyright John Doe
#
#  @defgroup OperationsPyTestSuite OperationsPyTestSuite
#  This test suite is about.
#  Any details
#  @remarks functional,integration
#  @{

import sys

## @test Full test
#  description of test_Add
#  @pre preconditions
#  @post post-conditions
#  @result expected results
#  @remarks negative,regression
#  @priority medium
def test_Add():
    assert 0 == 1, "Error message"
    return

## @test Full test
#  description of test_Multiply
#  @pre preconditions
#  @post post-conditions
#  @result expected results
#  @remarks negative,regression
#  @priority medium
def test_Multiply():
    assert 1 == 1, "Error message"
    return

## @test Full test
#  description
#  @pre preconditions
#  @post post-conditions
#  @result expected results
#  @remarks regression,positive,not_implemented
#  @priority medium
def test_PlannedButNotImplemented():
    assert 1 == 1, "Error message"
    return

# Optional main
def main():    
    test_Add()
    test_Multiply()
#     test_PlannedButNotImplemented()
    return 0

# Call main
if __name__ == "__main__":
    sys.exit(main())

## @}

