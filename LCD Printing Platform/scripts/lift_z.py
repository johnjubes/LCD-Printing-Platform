# File name: lift_z.py
# Author: John Jubenville
# Date created: 06/22/2021
# Date last modified: 06/23/2021
# Python Version: 3.9 / 2.7

# Function:
# lift_z.py is called after a layer is cured
# It lifts the plate by the set lift_distance by returning a line of g-code to NanoDLP

import sys
import csv
import pandas as pd

#set lift distance here (change to command line arg in NanoDLP)
lift_distance = 5.0

def get_File_Values():
    # get layer number from temp.csv (change this to command line arg if possible in NanoDLP)
    with open('temp.csv') as progress_file:
        line = progress_file.readline()
        split = line.split(",")

        current_layer = int(split[0])

    # get current z-axis height from test_layers.csv
    layers_data = pd.read_csv('test_layers.csv', sep=',').values
    new_z_pos = layers_data[current_layer][1]

    return new_z_pos 

def main():

    z_pos = str(get_File_Values() + lift_distance)
    sys.stdout.write('G1 Z' + z_pos)

main()
