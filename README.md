# RunTest

## Introduction:

More than just a script, the Scripts/RunTest.py is the pilar of a full Continuous Integration (CI) and Test Driven process, working with different languages and well-know test frameworks and specifically well designed for Agile Test Driven Methodology ([See ATDM](Doc/ATDM.md)).

It can be called from a CI build system such as Jenkins to insure that any changes in the code are automatically validated, and then generating for you a centralized test report, concatenating any test framework results into one clear and understandable report.

No need to maintain test specifications files, test sources, test reports, test synthesis anymore. It does it for you!

### RunTest Philosophy:

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

### RunTest strength:

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

## Licence

Free to use at your own responsibility.

## Get started

For the impatient.

- Clone the repo 
- Build Test/Gtest/main.cpp, Test/Gtest/OperationsCppTestSuite.cpp and the Test/Gtest/Gtest/ directory (Google test framework) to get a Gtest app up and running.
- Adapt Test/Commands.cfg to the location of your Gtest executable:
 - Adapt that line: "Location/Exe --gtest_filter=@SUITE.@CASE --gtest_output=xml:@RESULT"
- Go to Scripts/
- call "python RunTest.py -d ../Test/Gtest -c ../Test/Commands.cfg -r ../Test/TestReport.csv -s ../Test/TestSynthesis.csv"
- check the result files:
 - Test/TestReport.csv
 - Test/TestSynthesis.csv
 
For more:
- "python RunTest.py -h"

## Directory content

The project directories are made as if it was a normal C/C++ or java project on which you would run RunTest.
- README.md is that file
- Doxyfile is the doxygen config file for the test documentation generation
- Doc/
 * html/ contains the result of doxygen ran on the Test/ directory (See Doxyfile)
 * Mgt/ contains interesting process documents as the "Iteration Documentation" which explains this test process and a bit more (Free for you own info)
- Scripts/ contains the RunTest.py and its modules
 * Lib/ contains the modules used by RunTest.py
- Src/ contains fake source code that will be used as source under test.
- Test/ contains all the test framework templates compatible with RunTest.py and that you can copy. 

## RunTest documentation

[RunTest Documentation](Doc/RunTest.md)

## Agile Test Driven Methodology

The process motivating the RunTest philosophy. ([See ATDM](Doc/ATDM.md))

## Iterating Documentation

A way to handle iteration in your project's documentation using RunTest for test documentation. (See [Iterating Documentation](Doc/IteratingDoc.md))

## Jenkins integration

Integrate RunTest into your Jenkins jobs. (See [Jenkins Documentation](Doc/Jenkins.md))

## For RunTest developers

For who want to develop further RunTest.py. see [Development documentation](Doc/Dev.md)





