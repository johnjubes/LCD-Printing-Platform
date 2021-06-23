# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 06/23/2021
# Python Version: 3.9 / 2.7

# Function:
# clean.py is called by NanoDLP after a print is complete.
# It deletes the temp.csv file.

import os

def main():
    # delete temp.csv
    os.remove('/home/pi/printer/temp.csv')

main()
