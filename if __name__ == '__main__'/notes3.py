import module2

if __name__ == "__main__":
    print(__name__)

# output
# ********************
# __main__
# ********************
# we import module2 which means that file is executed first
# module2 has print(__name__) statement, but it's inside __name__=="__main__"
# from notes2.py we know that module file's __name__ is set to it's file name
# so if __name__=="__main__" in the module2.py file is False, we won't execute the print statement in the module2.py file
# in notes3.py file __name__ is equal to __main__, so print(__name__) in notes3.py file is executed and we get the output
