#!/usr/bin/python
import os
import sys
import shutil
def move():
	print ("broken")


def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
# Give the user some context.
print("\nWelcome to my file mover and deleter")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 for files")
    print("[2] Enter 2 for folders")
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        file2()
    elif choice == '2':
            remove(path)
    elif choice == 'q':
        print("\nHave a good day!")
    else:
        print("\nI don't understand that choice, please try again.\n")
