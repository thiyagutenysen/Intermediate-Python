# Syntax for importing a python file, eg., galoobo.py is "import galoobo"
import module1

print(__name__)

# we get two outputs
# ***************************
# module1
# __main__
# ***************************
# while we import module1.py is executed, so print(__name__) in that file is set to it's own main which is it's file name
# __name__ is set to __main__ for the file which we run, this files calls modules and code from other files,
# __name__ in those called files are set to their own file name
# These things are done by python before running the python file itself

# Summary
# __name__ is set to file name when the code in this file is called from another file
# __name__ is set to __main__ when this file is executed
# whenever we import a python file or module, then that is first executed before moving on to the next line
# therefore module1 is printed before __main__
