import re
import argparse
import sys


# Arguement Parsing for the show tech file name
parser = argparse.ArgumentParser()
parser.add_argument("-f",
                    help="""Enter the path and the filename
                    of show tech-support file""")

args = parser.parse_args()

if not args.f:
    print "-f <show tech file name> is mandatory"
    print "Sample Syntax is"
    print "shtech_extract.py -f ./show-tech/show_tech_file.log"
    sys.exit(2)

# read the show tech file
with open(args.f) as readfile:
    shtech = readfile.read()


def shtech_parse(command):
    # regex parsing
    pattern = command + "((?:.|\n)*?)------------- show"
    shtech_pattern = re.compile(pattern.encode('string-escape'))
    result = shtech_pattern.search(shtech).group()
    return result


def main():

    loop = True
    while loop is True:
        # Interactive prompter for the show commands
        command = raw_input("Enter the show command: ")

        # Exit the script when user input end
        if command.lower() != "end":
            # parse show tech for required output
            result = shtech_parse(command)

            # print Result
            for each_line in result.split("\n"):
                if each_line != "------------- show":
                    print each_line

        else:
            loop = False

if __name__ == "__main__":
    main()
