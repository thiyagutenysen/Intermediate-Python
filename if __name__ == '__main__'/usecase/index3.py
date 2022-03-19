import high_level_usecase3

# we can only run something that's inside module's __name__=="__main__" condition when
# we write all the statements inside main function in high_level_usecase3.py,
# and call the main() function inside __name__=="__main__"
# Then in our runnable python file ie.,
# index file we call module.main()X to run those statements inside __name__=="__main__" in the module
high_level_usecase3.main()

# output
# ********************
#  This line will always be run
# This file high_level_use_case2's main method
# ********************
