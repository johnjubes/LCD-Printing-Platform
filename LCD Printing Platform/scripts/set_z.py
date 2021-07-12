# File name: set_z.py
# Author: John Jubenville
# Date created: 06/22/2021
# Date last modified: 07/12/2021
# Python Version: 3.9 / 2.7

# Function:
# set_z.py is called at the start of each layer
# It moves the plate to the height specified in the layers.csv file by returning a line of g-code to NanoDLP

import sys
from reader import Reader

def main():
    reader = Reader()
    z_pos = str(reader.getZ_pos())
    sys.stdout.write('G1 Z' + z_pos)

main()
