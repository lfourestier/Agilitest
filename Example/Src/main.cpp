/**
 * @file main.cpp
 * @author John Doe
 * @date 2013
 * @copyright John Doe
 *
 * @mainpage
 * The program is about adding two integers.
 * @section Design Design
 * Some design consideration here.
 *
 * @section Tests Tests
 * @ref test reference the test list page\n
 * @ref MyTestSuite reference a test suite\n
 *
 * @section ToDos ToDos
 * @ref todo reference the todo list page\n
 *
 * @section PageRef Other pages
 * @ref Page1 reference to other independent pages\n
 * @ref Page2 reference to other independent pages\n
 *
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

//! The sky states
enum
{
    Sunny,     	//!> No Clouds at all
    Partially, 	//!> Partially cloudy, but more sun than cloud
    Cloudy,   	//!> More cloud than sunday
    Grey,       //!> No sun at all
    Foggy,     	//!> No sun and fog around
} SkyStates;

//! My variable
int MyGlobalVariable;

//! My Macro
#define MY_MACRO 1

/**
 * @brief Add two integers
 *  This function makes the sum of two integers
 * @param a: The first integer
 * @param b: The second integer
 * @return a+b
 * @notes This are my notes
 *
 * @todo To be done for float as well
 */
int AddInteger(int a, int b)
{
    return a + b;
}

/**
 * Main function
 * @return
 */
int main(int argc, char* argv[])
{
    return 0;
}

