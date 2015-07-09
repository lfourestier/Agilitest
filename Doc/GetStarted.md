# Get started

For the impatient! 

Running RunTest on Gtest framework example:
- Clone the repo
	- git clone https://github.com/lfourestier/Agilitest.git
	- git checkout develop
- cd Example/
- Build Test/Gtest (Google test framework) to get a Gtest app up and running.
	- cd Test/Gtest/Build
	- make
	- A Gtest executable is generated here
- If needed, adapt Test/Commands.cfg to the location of your Gtest executable:
	- Adapt that line: "Location/Exe --gtest_filter=@SUITE.@CASE --gtest_output=xml:@RESULT"
- Go to <repo>/Scripts/
- call "python RunTest.py -d ../Example/Test/Gtest -c ../Example/Test/Commands.cfg -r ../Example/Test/TestReport.csv -s ../Example/Test/TestSynthesis.csv"
- check the result files:
	- Example/Test/TestReport.csv
	- Example/Test/TestSynthesis.csv
 
For more options:
 - "python RunTest.py -h"

