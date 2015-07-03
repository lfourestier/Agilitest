# Jenkins integration

![Jenkins job](Doc/Jenkins.png)

## Setup a job

If you want to try RunTest with jenkins you can configure a job as follow.

### Source Code Management

Git repo:

	https://github.com/lfourestier/RunTest.git

Branch:

	refs/heads/develop

### Build Triggers

	"Poll SCM" -> H/1 * * * *
	
### Build
 
Execute shell:

	cd sw\RunTest\Test\Cunit\Build
	make clean all
	cd ..\..\Gtest\Build
	make clean all
	cd ..\..\..\Scripts
	@echo Starting RunTest
	c:\Python27\python.exe RunTest.py -d ../Test/Cunit,../Test/Gtest -c ../Test/Commands.cfg -r ../Test/TestReport.csv -s ../Test/TestSynthesis.csv
	
### Post-build Actions

**Artifacts:**
 - sw/RunTest/Test/*.csv
 
**Plot build data:** (Plot plugin required)
 - Data series file: sw/RunTest/Test/TestSynthesis.csv 
 - Exclude columns by name: Time,Duration
 - "Display original csv above plot"
