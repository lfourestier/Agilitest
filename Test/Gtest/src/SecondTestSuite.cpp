/**
 * @file SecondTestSuite.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup SecondTestSuite SecondTestSuite
 * This test suite is about.
 * Any details
 * @remarks regression,system
 * @{
 */

#include "SecondTestSuite.h"

void SecondTestSuite::SetUp(void) {

}

void SecondTestSuite::TearDown(void) {

}

/**
 * @test testAdd
 * Full test description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,system,integration,negative
 */
TEST_F(SecondTestSuite, testAdd)
{
    EXPECT_EQ(1, 1);
}

/**
 * @test testMultiply
 * Full test description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,system,integration,positive
 */
TEST_F(SecondTestSuite, testMultiply)
{
    EXPECT_EQ(1, 1);
}

/**
 * @test testPlannedButNotImplemented
 * Full test description
 * @pre preconditions
 * @post post-conditions
 * @result expected results
 * @remarks regression,system,integration,positive,NOT_IMPLEMENTED
 */
TEST_F(SecondTestSuite, testPlannedButNotImplemented)
{
    EXPECT_EQ(1, 1);
}

/** 
 * @}
 */
