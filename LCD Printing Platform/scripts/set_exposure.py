# File name: set_exposure.py
# Author: John Jubenville
# Date created: 07/12/2021
# Date last modified: 07/12/2021
# Python Version: 3.9 / 2.7

# Function:
# Returns the layer exposure time in seconds

from reader import Reader
import sys

def main():
    reader = Reader()
    exposure = str(reader.getExposure())
    sys.stdout.write(exposure)

main()