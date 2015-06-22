*** RunTest ***

* Introduction:

More than just a script, the Scripts/RunTest.py is the pilar of a full Agile Test Driven Development process, working with different languages and well-know test frameworks.

* Philosophy:

The philosophy is to simplify to the max the Agile Test Driven Development process:
- Minimizing the numbers of documents to edit
- Minimizing the number of process steps required
- Automatizing as max as possible
- Re-centering the work of anyone to the essential

* Key points:

Agile/scrum based:
- Based on User Story and iterations

Language agnostic:
- Java
- C
- Cpp
- Adaptible to any other languages if needed

Reuse well-known tools and frameworks:
- Doxygen
- Jenkins
- Test frameworks:
  - Google test
  - Junit
  - CppUnit
  - Cunit
  - ...
- Python
- Versionning
  - git
  - svn
  - ...

* Process details

Here is the Agile Test driven process that we follow:

- Grooming, refinement and iteration planning:
  - Follow the normal Agile process you are used to, to define your project USs and iteration plans
- Test driven user stories chronology:
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

