#include <stdio.h>
#include <stdlib.h>

#include <Basic.h>

#include "OperationsCTestSuite.h"

#define SUITE_ADD(suite, setup, teardown) {pSuite = CU_add_suite(#suite, setup, teardown); if (pSuite == NULL) {CU_cleanup_registry();return CU_get_error();}}
#define TEST_ADD(test) {if(CU_add_test(pSuite, #test, test) == NULL){CU_cleanup_registry();return CU_get_error();}}

int main(int argc, char **argv)
{
   CU_pSuite pSuite = NULL;
   CU_pTest pTest = NULL;

   /* initialize the CUnit test registry */
   if (CUE_SUCCESS != CU_initialize_registry())
      return CU_get_error();

   /* add a suite to the registry */
   SUITE_ADD(OperationsCTestSuite, Setup_OperationsCTestSuite, Teardown_OperationsCTestSuite);

   TEST_ADD(testAdd);
   TEST_ADD(testMultiply);
   TEST_ADD(testPlannedButNotImplemented);

   /* Run tests */
   CU_basic_set_mode(CU_BRM_VERBOSE);
   if (argc >= 3) {
	   pSuite = CU_get_suite(argv[1]);
	   pTest = CU_get_test(pSuite, argv[2]);
	   CU_basic_run_test(pSuite, pTest);
   }
   else {
	   CU_basic_run_tests();
   }

   CU_cleanup_registry();
   return CU_get_error();
}
