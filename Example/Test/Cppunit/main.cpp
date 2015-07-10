int main( int argc, char **argv)
{
  CppUnit::TextUi::TestRunner runner;
  runner.addTest( ExampleTestCase::suite() );
  runner.addTest( ComplexNumberTest::suite() );
  runner.run();
  return 0;
