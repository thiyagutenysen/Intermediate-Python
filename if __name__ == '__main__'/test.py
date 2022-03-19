def main():
    print(__name__)


# usual method
main()

# professional method
# we should write if __name__ == "__main__": only in the file which we run, not in the module or helper files
if __name__ == "__main__":
    main()
