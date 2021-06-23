# File name: set_z.py
# Author: John Jubenville
# Date created: 06/22/2021
# Date last modified: 06/23/2021
# Python Version: 3.9 / 2.7

# Function:
# set_z.py is called at the start of each layer
# It moves the plate to the height specified in the layers.csv file by returning a line of g-code to NanoDLP

import sys
import csv
import pandas as pd

def get_File_Values():
    # get layer number from temp.csv (change this to command line arg if possible in NanoDLP)
    with open('temp.csv') as progress_file:
        line = progress_file.readline()
        split = line.split(",")

        current_layer = int(split[0])

    # get layer height from test_layers.csv
    layers_data = pd.read_csv('test_layers.csv', sep=',').values
    new_z_pos = layers_data[current_layer][1]

    return new_z_pos

def main():

    z_pos = str(get_File_Values())
    sys.stdout.write('G1 Z' + z_pos)

main()
