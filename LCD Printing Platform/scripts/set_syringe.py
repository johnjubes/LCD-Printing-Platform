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

import serial
import time
from reader import Reader


def main():
    # get layer data from layers.csv
    reader = Reader()
    current_syringe_pos = reader.getLast_syringe_pos()
    new_syringe_pos = reader.getSyringe_pos()

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

main()
