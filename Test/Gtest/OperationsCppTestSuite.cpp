/**
 * @file OperationsCppTestSuite.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup OperationsCppTestSuite OperationsCppTestSuite
 * This test suite is about.
 * Any details
 * @remarks regression,system
 * @{
 */

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
 * @remarks requirements,regression,system,integration,negative
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
 * @remarks regression,system,integration,positive
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
 * @remarks regression,system,integration,positive,NOT_RUN
 * @priority medium
 */
TEST_F(OperationsCppTestSuite, testPlannedButNotImplemented)
{
    EXPECT_EQ(1, 1);
}

/** 
 * @}
 */
