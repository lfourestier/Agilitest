/**
 * @file CppunitTestSuite
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @defgroup CppunitTestSuite CppunitTestSuite
 * This test suite is about.
 * @remarks regression,system
 *  @{
 */

#ifndef MYCPPUNITTESTSUITE_H
#define MYCPPUNITTESTSUITE_H

#include <cppunit/extensions/HelperMacros.h>

class CppunitTestSuite: public CppUnit::TestFixture
{
    CPPUNIT_TEST_SUITE (MyCppunitTestSuite);
    CPPUNIT_TEST (testAdd);
    CPPUNIT_TEST (testMultipy);CPPUNIT_TEST_SUITE_END();

public:
    void setUp();
    void tearDown();

    void testAdd();
    void testMultiply();
};

#endif  // MYCPPUNITTESTSUITE_H
