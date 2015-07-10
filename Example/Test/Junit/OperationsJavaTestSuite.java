/**
 * @file OperationsJavaTestSuite.java
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup OperationsJavaTestSuite OperationsJavaTestSuite
 * This is a junit test suite.
 * @remarks regression,system
 *  @{
 */

package my.operations;

import static org.junit.Assert.assertEquals;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class OperationsJavaTestSuite {

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
	 * @remarks regression,system,integration,positive,not_implemented
	 * @priority medium
	 */
	@Test
	public void testPlannedButNotImplemented() {
	}
}

/**
 * @}
 */
