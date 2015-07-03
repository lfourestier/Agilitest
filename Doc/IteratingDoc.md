# Iterating documentation in agile

## Introduction
How do we keep a good documentation of a product/project in an agile world where the work is based on iteration, and then a “one shot” documentation is not possible?

## Principles
Agile/scrum is based on User Stories, which are as kind of atomic pieces of work for the team. 

Then...

 - **Let's document on “per US”.**
 - **Let's integrate the documentation in the CI.**
 	- The documentation should be part of the DoD then.
 - **Let's try to stick to the essential.**
 	- The documentation should remain simple to find, follow and update. 

## Main documents
Here are the main documents we may want to keep track in an iterating way:
 - Architecture
 - Design and implementation
 - Test

## Architecture documentation
The idea is to use Wiki pages for the architecture documentation.

**Advantages:**
 - It is centralized
 - It is easy to access, search, browse
 - It is simultaneous access compatible
 - It is versionned
 - It is backed up
 - It is commentable
 - We can attach files, images...

**Process:**
 - The architect to write its first architecture prior to development in Wiki
 - The developers to access the architecture Wiki pages at any time during the US.
 - If any issue found, the developers to comment the page with its feedback. 
 - The architect to revise its documentation based on the comments of the developers during US.
 - The developers to close the comments and apply the revised architecture in the implementation.

**Proposed structure:**
 - MainWikiPage
 	- ...
 	- Architecture
 		- Overview
 		- First module
 		- Second module
 		- …

## Design and implementation documentation
The idea is to use doxygen tool to keep up to date the design and implementation documents.

**Advantages:**
 - It is an obvious documentation place for the developers (as it is directly in the code)
 	- Less time loss in editing external documents
 - it is compatible with many languages
 	- C, C++, Java, C#...
 	- VHDL, XML... (Thus, even for hardware)
 	- …
 - It is automatizable 
 - It integrates perfectly in the CI processes
 	- Document is always kept up to date by Jenkins
 - It is centralized and automated by Jenkins
 - It is versionned
 - **Doxygen pages can be linked into Wiki**

**Inconvenients:**
 - Graphics and pictures are still difficult to integrate
 	- But not impossible

**Process:**
 - The developers to edit the comments while changing the implementation
 	- Don't forget the date of the file and the copyright if required
 - The reviewer to validate the documentation changes (meanwhile reviewing the code)
 - Jenkins to automatically rebuild the documentation when committed
 - The PO to accept the documentation from Jenkins while delivering the US

**Proposed structure:**

File documentation at the beginning of every files:
	/**
	* @file file.c
	* @author Sony Europe, Techsoft
	* @date 2013
	* @copyright Sony
	*/

Main page in the main source file (Ex: Main.c/cpp/java...):
	/*
	* @mainpage
	
	* The program is about adding two integers.
	
	* @section Design Design

	* Some design consideration here.
	
	*
	
	* @subsection Tests Tests
	
	* @ref test reference the test list page\n
	
	* @ref MyTestSuite reference a test suite\n
	
	* 
	
	* @subsection ToDo ToDos
	
	* @ref todo reference the todo list page\n
	
	
	*
	* @subsection PageRef Other pages
	
	* @ref Page1 reference to other independent pages\n
	
	* @ref Page2 reference to other independent pages\n
	
	* /

Independent pages any where it is relevant, after the file documentation (see below):
	/** 
	* @page Page1 A documentation page
	
	*   @tableofcontents
	
	*   Leading text.
	
	*   @section sec An example section
	
	*   This page contains the subsections @ref subsection1 and @ref subsection2.
	
	*   For more info see page @ref page2.
	
	*   @subsection subsection1 The first subsection
	
	*   Text.
	
	*   @subsection subsection2 The second subsection
	
	*   More text.
	
	* 
	
	* @page Page2 Another page
	
	*  Even more info.
	
	*/

Function documentation in any source files:
	/* 
	* @brief Add two integers
	*  This function makes the sum of two integers
	* @param a: The first integer
	* @param b: The second integer
	* @return a+b
	*/
	int AddInteger(int a, int b) {
	…}

Variable and macro documentation
	//! My variable
	int MyGlobalVariable;
	
	//! My Macro
	#define MY_MACRO 1

Enumeration, structure documentation:
	//! The sky states
	enum {
	Sunny,     //> No Clouds at all
	Partially, //> Partially cloudy, but more sun than cloud
	Cloudy,   //> More cloud than sunday
	Grey,       //> No sun at all
	Foggy,     //> No sun and fog around
	} SkyStates;

Notes and todo, in any of the previous doxygen comments:

	@notes Some additional notes and remarks
	@todo Any remaining task to be done here

## Test documentation
The idea is to use the combination of unit test frameworks (Ex, Cunit, cppunit, junit...), doxygen tool, the “Runtest” python script and jenkins to keep up to date the test documents (test plan and reports).

**“RunTest” python script:**
The “RunTest” python scripts is capable of parsing the test files (whatever language it is c, cpp, java…) in the specified test directories, extracting the test suites and cases comments, run each tests and generate a test plan/report in the csv form (excell compatible).
That script enables jenkins to automatically generate the test plan and report out of the latest test comment changes and test results.

**Advantages:**
 - It is an obvious documentation place for the developers/tester (as it is directly in the test code)
 	- Less time loss in editing external documents
 - It is automatizable in jenkins
 - It integrates perfectly in the CI processes
 	- Document is always kept up to date by Jenkins
 - It is centralized by Jenkins
 - It is versionned
 - **Doxygen pages can be linked into Wiki**

**Process:**
 - The tester to writes its test plan directly in the test code in doxygen format (See below doxygen comments)
	 - The tester prepares the skeleton of the test suites and cases (Empty test suite and case functions, but full description of the test suites/cases)
	 	- in C for c unit, in cpp for cpp unit...
	 - Planned tests are marked as “NotImplemented” at first
 - The “NotImplemented” tests are not run by the “RunTest” python script but the documentation is updated including newly planned tests.
 - The reviewer to validate the test plan
 - The developers/testers to implement the tests while in the US
 - The reviewer to validate the test implementation/documentation
 - jenkins to generate test plan and report
 - The PO to accept while delivering the US

**Proposed structure:**

The @remarks is used to “keyword” the test suites and cases (“RunTest” python script will then execute accordingly)

Test file header and test suite marker with @defgroup:
	/**
	
	* @file test.cpp
	
	* @author Sony Europe, Techsoft
	
	* @date 2013
	
	* @copyright Sony
	
	*
	
	* @defgroup MyTestSuite
	
	* This test suite is about.
	
	* @remarks regression,system
	
	*
	*  @{
	
	*/



Test cases 
	/**
	
	* @test First test case
	
	* Full test description
	
	* @pre preconditions
	
	* @post post-conditions
	
	* @result expected results
	
	* @remarks regression,system,integration,negative
	
	*/

	TEST(FactorialTest, Negative) {
	
	  EXPECT_EQ(1, 1);
	
	}



	/**
	
	* @test Positive test case
	
	* Full test description
	
	* @pre preconditions
	
	* @post post-conditions
	
	* @result expected results
	
	* @remarks regression,system,integration,positive
	,NotImplemented
	*/
	
	TEST(FactorialTest, Positive) {
	
	  EXPECT_EQ(1, 1);
	
	}



	/** 
	
	* @} 
	
	*/