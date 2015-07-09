# Agile Test Driven Methodology (ATDM)

Agile Test Driven Methodology is simple: "You define your User Story (US) acceptance tests before any anything else in your US lifecycle". 
Where a US acceptance test is a functional scenario prooving/validating one of your US requirements.

This could be like this:



## US Lifecycle in ATDM using RunTest

This is what a US lifecycle could be in ATDM using RunTest:
![ATDM User Story lifecycle](Doc/ATDM.png)

1. Define the US acceptance tests using the RunTest synthax directly into the test sources:
	* RunTest will detect automatically the changes and, through jenkins, update the test report with the newly specified tests.
2. Make your design for the feature to be implemented:
	* Use doxygen into your code to automate documentation for instance.
3. Implement acceptance tests within the same file where you specified them:
	* RunTest will again detect automatically the changes and, through jenkins, update the test report with the newly implemented test results (Most probably all failing without the functionality being implemented yet).
3. Implement your functionality:
	* RunTest will again detect automatically the changes and, through jenkins, update the test report with the new functionality test results.
	* Developers to add their own unit tests in the same way while developing/debugging. That will grow the test coverage at the same time through RunTest.
4. Demo your US to your PO
	* Simple!! Everything is then ready in Jenkins (test report, synthesis and documentation).
	* Just the DoD needs to be verified again for safety


