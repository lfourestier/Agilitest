import optparse
import sys

OK = 0
 
# Main
def main():
    # Parse options
    parser = optparse.OptionParser()

    parser.add_option("-d", "--directories",
                      dest="directories", help="Specify the comma separated list of directory where to find test suite files to parser.",
                      action="store", default='.');

    parser.add_option("-c", "--commands",
                      dest="commands", help="Specify the option configuration file to use. If not specified, no test will be run.",
                      action="store");

    parser.add_option("-g", "--generate",
                      help="Generate a option template config file that can be used as a seed. See also -c option.",
                      action="store_const", const=True, dest="generate")


    (options, args) = parser.parse_args()
    print(str(options))
    
    return OK
    
# Call main
if __name__ == "__main__":
    sys.exit(main())
