# Agile Test Driven Methodology (ATDM)

Agile Test Driven Methodology is simple: "You define your User Story (US) acceptance tests before any anything else in your US lifecycle". 
Where a US acceptance test is a functional scenario prooving/validating one of your US requirements.
It could be: 
- Behavioral Driven Development:
 - Given...
 - When...
 - Then...
- Model based Testing
- Or just simple hand written scenarios.

Up to you.

## US Lifecycle in ATDM using RunTest

As a summary, this is what a US lifecycle could be in ATDM using RunTest:
1. Define the US acceptance tests using the RunTest synthax directly into the test sources.
 * RunTest will detect automatically the changes and, through jenkins, update the test report with the newly specified tests.
2. Implement acceptance tests within the same file
 * RunTest will again detect automatically the changes and, through jenkins, update the test report with the newly implemented test results (Most probably all failing without the functionality being implemented).
3. Implement your functionality
 * RunTest will again detect automatically the changes and, through jenkins, update the test report with the new functionality test results.


