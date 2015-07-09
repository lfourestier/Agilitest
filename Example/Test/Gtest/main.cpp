/**
 * @file main.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 */

#include <iostream>
using namespace std;

#include "gtest/gtest.h"

int main(int argc, char **argv) {
	cout << "Run Gtest" << endl;
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
