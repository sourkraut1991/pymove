#!/usr/bin/python
import os
import sys
import shutil
def file():
## Get input ##
    myfile= raw_input("Enter file name to delete: ")

## Try to delete the file ##
try:
    os.remove(myfile)
except OSError as e:  ## if failed, report it back to the user ##
    print ("Error: %s - %s." % (e.filename, e.strerror))


def folder():
# Get directory name
    mydir= raw_input("Enter directory name: ")

## Try to remove tree; if failed show an error using try...except on screen
try:
    shutil.rmtree(mydir)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

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
        Prob1()
    elif choice == '2':
            Prob2()
    elif choice == 'q':
        print("\nHave a good day!")
    else:
        print("\nI don't understand that choice, please try again.\n")
