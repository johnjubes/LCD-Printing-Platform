# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 05/09/2021
# Python Version: 3.9

# setup_layer is called by NanoDLP before each layer begins to print
# It determines if a change should be made to the syringe, calculates what the change is (consider moving the calculations to preprocessing),
# then calls the move function from the Syringe class.
# Then it returns the Z axis G-code to NanoDLP (if that's possible), this allows us to "trick"
# the printer into printing to the same layer height twice.

# To Do:
#   Make calulations from prefered mix input to arduino output (move this to preprocessing at some point?)
#   Format Z axis output to match NanoDLP expectations

import pandas as pd
import csv
from syringe_class import Syringe


# method reads position info from the temp.csv and layers.csv files
def get_File_Values():
    # get layer number and position from progress.tmp (change this to command line arg if possible in NanoDLP)
    with open('temp.csv', newline='') as progress_file:
        line = progress_file.readline()
        split = line.split(",")
        split2 = split[1].split("\r")

        current_layer = int(split[0])
        current_syringe_pos = float(split2[0])

    # get current layer data from layers.csv
    layers_data = pd.read_csv('../layer_profiles/test_layers.csv', sep=',').values
    new_z_pos = layers_data[current_layer][1]
    new_mix = layers_data[current_layer][2]

    # get last layer data from layers.csv
    if (current_layer > 0):
        last_z_pos = layers_data[current_layer - 1][1]
        last_mix = layers_data[current_layer - 1][2]
    else:
        last_z_pos = 0.0
        last_mix = 0.0

    return current_layer, current_syringe_pos, new_mix, new_z_pos, last_mix, last_z_pos


def calculate_Syringe_Position(new_mix):
    # convert whatever the input is (ratio, concentration, etc) to syringe position
    output = new_mix
    return output


def main():
    # get layer number and position from progress.tmp (change this to command line arg if possible in NanoDLP)
    # get layer data from layers.csv
    current_layer, current_syringe_pos, new_mix, new_z_pos, last_mix, last_z_pos = get_File_Values()

    # Calculate new syringe position (will flesh out math later)
    if (new_mix != last_mix):
        new_syringe_pos = calculate_Syringe_Position(new_mix)

        # Send new position to Arduino via serial, wait for move to finish
        syringe = Syringe()
        syringe.setPosition(new_syringe_pos)
        syringe.moveToPosition()
    else:
        new_syringe_pos = current_syringe_pos

    # update progress.tmp
    with open('temp.csv', 'w', newline='') as progress_file:
        writer = csv.writer(progress_file)
        writer.writerow([current_layer + 1, new_syringe_pos])

    # return Z height to NanoDLP (how this is done will depend on when NanoDLP drives the z/how NanoDLP receives script outputs)
    if (new_z_pos != last_z_pos):
        print('Move Z position to', new_z_pos)
    else:
        print('Keep Z position at', new_z_pos)
    return new_z_pos


main()
