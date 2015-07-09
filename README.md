# Agilitest

Quick shortcuts:
- [Agile Test Driven Methodology](Doc/ATDM.md)
- [Get Started](Doc/GetStarted.md)
- [Licenses](Doc/License.md) (Basically, "Free to use at your own responsibility")
- [Project Content](Doc/ProjectContent.md)
- [RunTest Usage Documentation](Doc/RunTest.md)
- [RunTest Development Documentation](Doc/Dev.md)
- [Jenkins Integration Documentation](Doc/Jenkins.md)
- [Doxygen Generation](Doc/Doxygen.md)
- [Iterating Documentation Methodology](Doc/IteratingDoc.md)

See "How To" chapter below as well.

## Introduction:

Agilitest is a full test driven methodology for Agile, articulated around a script (Scripts/RunTest.py) that optimizes the work of everybody in an agile and test driven way. 
([See "Agile Test Driven Methodology"](Doc/ATDM.md))

## RunTest script

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

## Agile Test Driven Methodology

The process motivating the RunTest philosophy. ([See ATDM](Doc/ATDM.md))

## How To

- How to use Runtest.py : [RunTest Documentation](Doc/RunTest.md)
- How to develop RunTest.py :[Development documentation](Doc/Dev.md)
- How to integrate RunTest.py into Jenkins : [Jenkins Documentation](Doc/Jenkins.md))

## Iterating Documentation

A way to handle iteration in your project's documentation using RunTest for test documentation. (See [Iterating Documentation](Doc/IteratingDoc.md))





