/**
 * @file GtestTestSuite.h
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 */

#include "gtest/gtest.h"

class GtestTestSuite : public testing::Test {
	  virtual void SetUp();
	  virtual void TearDown();
};
