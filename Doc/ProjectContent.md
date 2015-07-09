# Project content

The project contains:
- README.md : the top readme file.
- Doc/
 	- The secondary readme files
- Scripts/ contains the RunTest.py and its modules
 	- Lib/ contains the modules used by RunTest.py
- Example/ : This directory is made as if it was your normal C, C++ or java project on which you would apply Agilitest.
	- Doc/
		- html/ contains the result of doxygen ran on the Test/ directory (See Doxyfile)
	- Src/ contains fake source code that will be used as source under test.
	- Test/ contains all the test framework templates compatible with RunTest.py and that you can copy.
		- CppUnit : The CPP unit test framework templates
		- Cunit : The CUnit test framework templates 
		- Gtest  : The Google test framework templates 
		- Junit  : The Junit test framework templates 
		- Commands.cfg : The command.cfg templates (See [Runtest Documentation](RunTest.md) or [RunTest Development Documentation](Dev.md))
		- TestReport.csv : A generated report example
		- TestSynthesis.csv : A synthesis report example
	- Doxyfile is the doxygen config file for the test documentation generation

