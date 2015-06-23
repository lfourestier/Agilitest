/**
 * @file GtestTestSuite.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup GtestTestSuite GtestTestSuite
 * This test suite is about.
 * Any details
 * @remarks regression,system
 * @{
 */

#include "GtestTestSuite.h"

void GtestTestSuite::SetUp(void) {

}

void GtestTestSuite::TearDown(void) {

}

/**
 * @test Full test
 * description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks requirements,regression,system,integration,negative
 * @priority medium
 */
TEST_F(GtestTestSuite, testAdd)
{
	EXPECT_EQ(1, 0);
}

/**
 * @test Full test
 * description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,system,integration,positive
 * @priority medium
 */
TEST_F(GtestTestSuite, testMultiply)
{
    EXPECT_EQ(1, 1);
}

/**
 * @test Full test
 * description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,system,integration,positive,NOT_IMPLEMENTED
 * @priority medium
 */
TEST_F(GtestTestSuite, testPlannedButNotImplemented)
{
    EXPECT_EQ(1, 1);
}

/** 
 * @}
 */
