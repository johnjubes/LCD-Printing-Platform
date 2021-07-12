# File name: Reader.py
# Author: John Jubenville
# Date created: 07/12/2021
# Date last modified: 07/12/2021
# Python Version: 3.9 / 2.7

# Function:
# Contains the Reader class which returns values from layers.csv and temp.csv

import pandas as pd

class Reader: 
    def __init__(self):

        # get layer number and syringe pos from temp.csv
        with open('temp.csv') as progress_file:
            line = progress_file.readline()
            split = line.split(",")
            split2 = split[1].split("\r")

            current_layer = int(split[0])
            self.last_syringe_pos = float(split2[0])

        # get current layer values from test_layers.csv
        layers_data = pd.read_csv('layers.csv', sep=',').values

        self.current_layer = current_layer
        self.z_pos = layers_data[current_layer][1]
        self.syringe_pos = layers_data[current_layer][2]
        self.exposure_time = layers_data[current_layer][3]

        
    def getCurrent_layer(self):
        return self.current_layer

    def getZ_pos(self):
        return self.z_pos

    def getSyringe_pos(self):
        return self.syringe_pos

    def getLast_syringe_pos(self):
        return self.last_syringe_pos

    def getExposure(self):
        return self.exposure_time