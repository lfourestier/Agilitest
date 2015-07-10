/**
 * @file OperationsCppTestSuite.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup OperationsCppTestSuite OperationsCppTestSuite
 * This test suite is about.
 * Any details
 * @remarks functional,system
 * @{
 */

#include <unistd.h>

#include <OperationsCppTestSuite.h>

void OperationsCppTestSuite::SetUp(void) {

}

void OperationsCppTestSuite::TearDown(void) {

}

/**
 * @test Full test
 * description of testAdd
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks negative,regression
 * @priority medium
 */
TEST_F(OperationsCppTestSuite, testAdd)
{
	sleep(1);
	EXPECT_EQ(1, 0);
}

/**
 * @test Full test
 * description of testMultiply
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,positive
 * @priority medium
 */
TEST_F(OperationsCppTestSuite, testMultiply)
{
    EXPECT_EQ(1, 1);
}

/**
 * @test Full test
 * description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,positive,not_implemented
 * @priority medium
 */
TEST_F(OperationsCppTestSuite, testPlannedButNotImplemented)
{
    EXPECT_EQ(1, 1);
}

/** 
 * @}
 */
