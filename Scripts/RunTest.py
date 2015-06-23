# Author Luc Fourestier (luc.fourestier@gmail.com)
#
# RunTest -d Cppunit,Junit,Gtest,Cunit -c Commands.cfg -r TestReport.csv -s TestsSynthesis.csv

import optparse
import sys
import os
import ConfigParser

# Constant
OK = 0
ERROR = -1

# Generate a template command config file
def generate_command_config(config_file):
    gen_file = open(config_file, 'w')
    gen_file.write(command_config_file)
    gen_file.close()
    print "Generated " + config_file
    return 0
    
command_config_file = """# Author Luc Fourestier (luc.fourestier@gmail.com)
#
# Specify the commands to be applied for each test frameworks in order to run the tests one by one.
#
# Supported framework so far:
# Gtest
# Junit
# Cppunit
# Cunit
#
# @@ separated commands: 
# "<command1> @@ <command2> @@ <command3>" and so on...
# Where: 
# <command> is a normal command line (Ex: echo "Hello world!")
# In which:
# @CASE will be replaced by the test case name
# @SUITE will be replaced by the test suite name
# Ex: "echo Run @CASE in @SUITE @@ echo Done"
#
# Commands are then run one after each other.
#
# After each test case run, the intermediate result file is specified with the "result" param.

[Gtest]
command = echo "Run Gtest case @CASE in @SUITE" @@ echo "Done!"
result = result.xml

[Junit]
command = echo "Run Junit case @CASE in @SUITE" @@ echo "Done!"
result = result.xml

[Cppunit]
result = result.xml
command = echo "Run Cppunit case @CASE in @SUITE" @@ echo "Done!"

[Cunit]
command = echo "Run Cunit case @CASE in @SUITE" @@ echo "Done!"
result = result.xml
"""

# Main
def main():
#     print "# RunTest #"
    
    Log.SetLevels([Log.ERROR, Log.WARNING, Log.DEBUG])
    
    # Parse options
    parser = optparse.OptionParser()

    parser.add_option("-d", "--directories",
                      dest="directories", help="Specify the comma separated list of directory where to find test suite files to parser.",
                      action="store", default='.');

    parser.add_option("-c", "--commands",
                      dest="commands", help="Specify the option configuration file to use. If not specified, no test will be run.",
                      action="store");

    parser.add_option("-r", "--report",
                      dest="report", help="Specify the test report file where to write back the results in CSV format.",
                      action="store", default='TestReport.csv');

    parser.add_option("-i", "--include",
                      dest="include", help="Specify the tests and suites to be ran, based on keywords (See @remarks). ex: \"regression,integration\"",
                      action="store");

    parser.add_option("-x", "--exclude",
                      dest="exclude", help="Specify the tests and suites NOT to be ran, based on keywords (See @remarks). ex: \"NOT_IMPLEMENTED\"",
                      action="store");

    parser.add_option("-s", "--synthesis",
                      dest="synthesis", help="Specify the synthesis file where to concatenate back the tests synthesis (run, pass, fail) in CSV format.",
                      action="store", default='TestSynthesis.csv');

    parser.add_option("-g", "--generate",
                      help="Generate a option template config file that can be used as a seed. See also -c option.",
                      action="store_const", const=1, dest="generate")

    (options, args) = parser.parse_args()
    
    # Generate template option file
    if options.generate == 1:
        commands = "Commands.cfg"
        if options.commands:
            commands = options.commands
        generate_command_config(commands)
        return OK

    # Parse directory list
    dir_list = options.directories.split(',')
    Log.Log(Log.DEBUG, "Directory list = " + repr(dir_list))
    
    # Parse option file
    command_dict = dict()
    if options.commands:
        config = ConfigParser.ConfigParser()
        config.readfp(open(options.commands))
        for section in config.sections():
            option_dict = dict()
            for option in config.options(section):
                option_dict[option] = config.get(section, option)
            if option_dict:
                command_dict[section] = option_dict
            
        Log.Log(Log.DEBUG, "Commands = " + repr(command_dict))
    
    # Create test bench
    bench =  TestBench(dir_list, command_dict, options.report, options.synthesis)
    
    # Parse tests
    bench.Parse()
    
    # Run tests
    bench.Run()

    return OK
    
# Call main
if __name__ == "__main__":
    sys.path.append("Lib")
    import TestGlobal
    import Log
    from TestBench import TestBench
    sys.exit(main())
