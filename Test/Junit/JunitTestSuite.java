/**
 * @file JunitTestSuite.java
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup JunitTestSuite JunitTestSuite
 * This is a junit test suite.
 * @remarks regression,system
 *  @{
 */

package my.operations;

import static org.junit.Assert.assertEquals;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class JunitTestSuite {

	/**
	 * @test Full test
	 * description
	 * @pre preconditions
	 * @post post-conditions
	 * @result expected results
	 * @remarks regression,system,integration,negative
	 * @priority medium
	 */
	@Test
	public void testAdd() {
		assertEquals("Add", 1, 1);
	}

	/**
	 * @test Full test 
	 * description
	 * @pre preconditions
	 * @post post-conditions
	 * @result expected results
	 * @remarks regression,system,integration,negative
	 * @priority medium
	 */
	@Test
	public void testMultiply() {
		assertEquals("Multiply", 1, 1);
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
	@Test
	public void testPlannedButNotImplemented() {
	}
}

/**
 * @}
 */
