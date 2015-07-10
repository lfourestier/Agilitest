# Development

If you want to develop, here is the correct place to learn RunTest

## Locations

All RunTest python code is in Scripts/

- Scripts/
 - RunTest.py = The main scripts responsible of the CLI. Converts CLI inputs into proper variables for TestBench.py (The main module)
 - Lib/
 	- TestBench.py is the central class that controls all the others. It provides:
 	 	-  TestBench.Parse()
 	 	-  TestBench.Run()
 	 	-  TestBench.GenerateReports()
 	- TestSuite.py is the suite container class containing all the info/fields of a suite. It provides:
 	 	- TestSuite.ParseHeader() that parse a suite header string and fill the fields
 	- TestCase.py is the case container class containing all the info/fields of a case. It provides:
 	 	- TestCase.ParseHeader() that parse a case header string and fill the fields
 	- TestCommand.py is the command parser and providers (See Commands.cfg). It provides:
 	 	- TestCommand.CheckValidity() to check commands validity in the .cfg file
 	 	- TestCommand.ExecuteTest() that execute a test case, finding the proper commands to apply to it
 	- TestFilter.py is the filter class that provides:
 	 	- TestFilter.IsSuiteIncluded() to check if a specific suite is part of the run and report
 	 	- TestFilter.IsCaseIncluded() to check if a specific case is part of the run and report
 	- TestResult.py is the result container class that provides result parsing. It provides:
 	 	- TestResult.ParseOutput() to parse command output and fill the result fields.
 	 	- TestResult.ParseResult() to parse intermediate result file (If generated) and fill the result fields.
 	- TestReports.py is the report generator class. It provides:
 	 	- TestReports.CreateCsvReport() to create a SemiColon Separated Values report compatible with excel or other tables
 	 	- TestReports.CreateJunitReport() NOT DONE YET
 	 	- TestReports.UpdateSynthesisReport() to append the synthesis of the new run to an existing synthesis file (or create it if does not exists)
 	- TestGlobal.py contains some general definitions
 	- Log.py provides simple logging functionality
 	
## Adding a new test framework

RunTest currently support Gtest, CppUnit, Cunit, Pytest and Junit frameworks.
Here are the points to add new supports.

What to change:
 - TestGlobal.py - Add new test framework type (Ex: CUNIT_TYPE)
 - Commands.cfg
  * Add a new section for the new framework (As defined in TestGlobal.py)
 - TestBench.py 
  * TestBench.CheckIsTestSuiteFile() - Add the new extension.
  * TestBench.SniffFile() - Add a new sniffer to detect the test suite type for that new framework (For example, see SniffGtest, SniffJunit...)
  * XXX_SUITE_REGEXP - Add new regular expression to detect suite and case comments in the new framework format
  * XXX_CASE_REGEXP_LIST
  * TestBench.ParseFileType() - To use those new regular expressions
 - TestResult.py
  * TestResult.ParseOuput() - Add a new ouput parser for the framework
  * TestResult.ParseResult() - Potentially, add new result parser as well
  * TestResult.SniffResult() - So you also need to change the result sniffer to detect the result type.
  
## Commands.cfg

	 Free to use at your own responsibility
	
	 Specify the commands to be applied for each test frameworks in order to run the tests one by one.
	
	 Supported framework so far:
	 Gtest
	 Junit
	 Cppunit
	 Cunit
	
	 @@ separated commands: 
	 "<command1> @@ <command2> @@ <command3>" and so on...
	 Where: 
	 <command> is a normal command line (Ex: echo "Hello world!")
	 In which:
	 @CASE will be replaced by the test case name
	 @SUITE will be replaced by the test suite name
	 @RESULT will be replaced by the result string specified in the optional "result" param.
	 Ex: "echo Run @CASE in @SUITE @@ echo Done"

	 Commands are then run one after each other.

	 After each test case run, the intermediate result file is specified with the "result" param.
	 if not specified, only the output will be parsed.
	
	 [Gtest]
	 command = echo "Run Gtest case @CASE in @SUITE" @@ echo "Done!"
	 result = ../Test/result.xml
	
	 [Junit]
	 command = echo "Run Junit case @CASE in @SUITE" @@ echo "Done!"
	 result = ../Test/result.xml
	
	 [Cppunit]
	 command = echo "Run Cppunit case @CASE in @SUITE" @@ echo "Done!"
	 result = ../Test/result.xml
	
	 [Cunit]
	 command = echo "Run Cunit case @CASE in @SUITE" @@ echo "Done!"
	 result = ../Test/result.out
 