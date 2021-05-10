# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 05/09/2021
# Python Version: 3.9

# clean.py is called by NanoDLP after a print is complete.
# It deletes the temp.csv file, and resets/powers down components as needed.

# To Do:
#   Determine what is needed for resets/shutdowns and implement

import os

def main():
    # delete temp.csv
    os.remove('temp.csv')

    # reset syringe position if needed

    # turn off arduino and other components if needed

main()