# RunTest

## Introduction:

More than just a script, the Scripts/RunTest.py is the pilar of a full Continuous Integration (CI) and Test Driven process, working with different languages and well-know test frameworks and specifically well designed for Agile Test Driven Methodology.

It can be called from a CI build system such as Jenkins to insure that any changes in the code are automatically validated, and then generating for you a centralized test report, concatenating any test framework results into one clear and understandable report.

No need to maintain test specifications files, test sources, test reports, test synthesis anymore. It does it for you!

## Agile Test Driven Methodology (ATDM)

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

### US Lifecycle in ATDM using RunTest

As a summary, this is what a US lifecycle could be in ATDM using RunTest:
1. Define the US acceptance tests using the RunTest synthax directly into the test sources.
 * RunTest will detect automatically the changes and, through jenkins, update the test report with the newly specified tests.
2. Implement acceptance tests within the same file
 * RunTest will again detect automatically the changes and, through jenkins, update the test report with the newly implemented test results (Most probably all failing without the functionality being implemented).
3. Implement your functionality
 * RunTest will again detect automatically the changes and, through jenkins, update the test report with the new functionality test results.


## RunTest Philosophy:

The RunTest philosophy is to simplify to the max the overheads:
- Minimizing the numbers of documents to edit
 - Indeed, with RunTest, the test specification is done inside the test code directly, no extra files to maintain needed then.
 - Runtest will generate the test specification file for you.
 - Test report and test spec are now concatenated into one generated file (Do we need more finally?)
- Minimizing the number of process steps required to validate the US
 - Runtest automates any "not needed" manual interventions.
- Automatizating as max as possible
 - RunTest is an automation.
- Centralizing the test specs, runs and results
 - One report, one synthesis which gather all the information, that's all.
- Re-centering the work of anyone to the essential
 - RunTest helps to re-center the attention of the team to the functionality to develop and nothing else.

## RunTest strength:

Agile/scrum:
- Fits into User Story and iterations

Continuous Integration and Test Driven philosophy

Language agnostic:
- Java
- C
- Cpp
- Adaptible to any other languages if needed

Reuse well-known tools and frameworks:
- Doxygen based synthax
- Jenkins based automation
- Test frameworks supported:
  - Google test
  - Junit
  - CppUnit
  - Cunit
  - ...
- Written in Python
 - Multiplatform compatibility
- Versionning compatible
  - git
  - svn
  - ...

## RunTest obligations

* RunTest uses the concept of test suites and test cases
* Each suites MUST in a separate file. 
* RunTest test suite names MUST finish by "TestSuite", then suite file name the same, ie: xxxxTestSuite.yyy
* RunTest test case names MUST start with "test", ie: "testxxxx"
* All test suites and cases MUST be documented according the RunTest documentation synthax (Doxygen compatible)
  * See the template file in Test/<Framework>/xxxTestSuite.yyy
  
## RunTest Process details

Here is the ATDM process that RunTest is best suited for:

- Grooming, refinement and iteration planning:
  - Follow the normal Agile process you are used to, to define your project USs and iteration plans
- ATDM chronology:
  - The team start a US
  - The test engineers write the skeleton/specs of the tests required to "proove" the US:
     - They create the xxxxTestSuite.yyy files (Depending on the test framework to be used in the project)
     - They feedback the architects if any issues already detected
     - They write the test header comments and definitions as required by RunTest (See templates)
     - They make sure that they fail for mandatory tests or they are marked as NOT_IMPLEMENTED (And not run) for optional tests
     - They commits/check-in those new files 
  - Jenkins will run those new tests
     - Jenkins will be RED for the new mandatory tests that are not yet implemented
     - Jenkins produces new test specification incorporating the newly defined tests (In csv or xml format)
     - Jenkins can produce graphical statistics
  - The test implementers start implementing the tests:
     - They implement the test within the skeleton files already written
     - Optionally, they can start writing the development skeleton with empty functions
     - Tests are still failing as there are not yet any implementation
  - The developers start implementing
     - They focus on implementing the functionalities and solving the failing tests
     - They feedback the testers and architects if any issues
     - Test become GREEN
  - The test engineers to correct the tests if:
     - The coverage is not enough
     - The requirements were finally not fully tested
     - ...
  - The Product Owner to accept the US
     - Based on Jenkins results

## RunTest Documentation Synthax (Doxygen compatible)

Notes: The doxygen tags are used with '@' prefix only.

### Suite file documentation:

	/**
	 * @file xxxxTestSuite.yyy
	 * @author John Doe
	 * @date 2013
	 * @copyright John Doe
	 *
	 * @defgroup xxxxTestSuite xxxxTestSuite
	 * This is a test suite description.
	 * @remarks regression,system
	 *  @{
	 */
	 
	[...]
	
	/**
	 * @}
	 */
	 
Notes: The comment tags (Ie: "/*" or "//" or "#") are language dependent. Here is a C/C++ example!

* @defgroup is used to specify the suite name
* Followed, the line below, by the test sute description
* @remarks tag is used for the filtering keywords (a coma separated list of keywords used to filter the tests)

### Case documentation

	/**
	 * @test Full test 
	 * description
	 * @pre preconditions
	 * @post post-conditions
	 * @result expected results
	 * @remarks regression,system,integration,negative
	 * @priority medium
	 */

Notes: The comment tags (Ie: "/*" or "//" or "#") are language dependent. Here is a C/C++ example!

* @test is used for the full test case descriptions. In Bdd, it could be the "When"
* @pre is used for the preconditions. In BDD, it could be the "Given"
* @post is used for the post-conditions. In BDD, it could be the "Then"
* @result is used for the expected result description
* @remarks tag is used for the filtering keywords (a coma separated list of keywords used to filter the tests)
* @priority (Not doxygen compatible) is used to given to some priority flavor to the test suite or case (ex: low, medium, high OR 1, 2, 3..., as you want!).

