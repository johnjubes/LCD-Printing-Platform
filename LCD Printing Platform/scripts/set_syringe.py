# File name: init_print.py
# Author: John Jubenville
# Date created: 06/23/2021
# Date last modified: 05/09/2021
# Python Version: 3.9 / 2.7

# Function:
# setup_layer.py is called by NanoDLP before each layer begins to print.
# It determines if a change should be made to the syringe position, 
# then calls the move function on the Arduino via serial.

# Setup:
# Enter serial ID here
serial_id = '/dev/ttyACM1'

import pandas as pd
import csv
import serial
import time


# method reads position info from the temp.csv and layers.csv files
def get_File_Values():
    # get layer number and position from progress.tmp (change this to command line arg if possible in NanoDLP)
    with open('temp.csv') as progress_file:
        line = progress_file.readline()
        split = line.split(",")
        split2 = split[1].split("\r")

        current_layer = int(split[0])
        current_syringe_pos = float(split2[0])

    # get current layer data from test_layers.csv
    layers_data = pd.read_csv('test_layers.csv', sep=',').values
    new_z_pos = layers_data[current_layer][1]
    new_syringe_pos = layers_data[current_layer][2]

    # get last layer data from layers.csv
    if (current_layer > 0):
        current_z_pos = layers_data[current_layer - 1][1]
    else:
        current_z_pos = 0.0

    return current_layer, current_syringe_pos, new_syringe_pos 


def main():
    # get layer number and position from progress.tmp (change this to command line arg if possible in NanoDLP)
    # get layer data from layers.csv
    current_layer, current_syringe_pos, new_syringe_pos = get_File_Values()

    # Adjust Syringe Position
    if (new_syringe_pos != current_syringe_pos):

        #calulate move in rotations
        move = new_syringe_pos - current_syringe_pos

        #convert new_syringe_position to string message
        out_str = str(move) + "\n"
        out = bytes(out_str)

        # Send new position to Arduino via serial, wait for move to finish
        ################################################################## 
        messages = 0
        while messages < 2:
		    ser = serial.Serial('/dev/ttyACM1', 9600, timeout = 1)
		    ser.flush()

		    ser.write(out)

		    if ser.in_waiting > 0:
		        line = ser.readline().decode('utf-8').rstrip()
		        #print(line)
		    messages = messages + 1
		    time.sleep(1)
	    ##################################################################
        
        #Wait for move to finish
        time.sleep(abs(int(move))*4)


    # update progress.tmp (moved to update_layer.py)
   # with open('temp.csv', 'w') as progress_file:
    #    writer = csv.writer(progress_file)
     #   writer.writerow([current_layer + 1, new_syringe_pos])

main()