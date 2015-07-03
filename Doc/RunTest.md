# RunTest usage

## RunTest commands

	Usage: RunTest.py [options]
	
	Options:
	  -h, --help            show this help message and exit
	  -d DIRECTORIES, --directories=DIRECTORIES
	                        Specify the comma separated list of directory where to
	                        find test suite files to parser.
	  -c COMMANDS, --commands=COMMANDS
	                        Specify the command file to use for the test run. If
	                        not specified, no test will be run (Only parsed). See
	                        -g option to generate a template command file.
	  -i INCLUDE, --include=INCLUDE
	                        Specify the inclusive filter (Coma separated list of
	                        keywords), ie: tests to be run based on keywords. ex:
	                        "regression,integration"
	  -x EXCLUDE, --exclude=EXCLUDE
	                        Specify the exclusive filter(Coma separated list of
	                        keywords), ie: tests NOT to be run based on keywords.
	                        ex: "regression,integration"
	  -r REPORT, --report=REPORT
	                        Specify the test report file where to write back the
	                        results in CSV format.
	  -s SYNTHESIS, --synthesis=SYNTHESIS
	                        Specify the synthesis file where to concatenate back
	                        the tests synthesis (run, pass, fail) in CSV format.
	  -g, --generate        Generate a template command file that can be used as a
	                        seed for your own commands. See also -c option.


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

## RunTest command file

The command.cfg contains the shell commands that will be executed by RunTest when finding a test case to run.
It can be specified by the "-c" option of RunTest.
To help you, a template command.cfg file can be generated by the "-g" option.

It is, per test framework, a list a commands separated by @@.
In those commands:
- @SUITE will be replaced by the suite name to be ran
- @CASE will be replace by the test case name to be ran
- @RESULT will be replaced by the intermediate result file (See "result" variable in the confiug file).

It also specify where to find the intermediate result file for the test case run.

## RunTest reports

### Test report and specification

RunTest creates a csv file out of all the information it gathers while parsing and running. It is excel compatible and can be inserted in any documents.
It replaces the specification and the test report.

### Test synthesis

The synthesis is a summary of the specified;run;pass;fail.. tests for the run. 
At every run, it is appending the new results, that enables the user to follow up the progression of the tests during the project. 
