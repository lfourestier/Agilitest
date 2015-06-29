/**
 * @file OperationsCTestSuite.c
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup OperationsCTestSuite OperationsCTestSuite
 * This test suite is about.
 * Any details
 * @remarks regression,system
 * @{
 */

#include <unistd.h>

#include <CUnit.h>

#include "OperationsCTestSuite.h"

int Setup_OperationsCTestSuite(void)
{
	return 0;
}

int Teardown_OperationsCTestSuite(void)
{
	return 0;
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
void testAdd(void)
{
	CU_ASSERT(0 == 1);
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
void testMultiply(void)
{
	CU_ASSERT(1 == 1);
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
void testPlannedButNotImplemented(void)
{
	CU_ASSERT(1 == 1);
}

/**
 * @}
 */
