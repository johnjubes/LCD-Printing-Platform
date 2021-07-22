# File name: mix_syringe.py
# Author: John Jubenville
# Date created: 07/19/2021
# Date last modified: 07/19/2021
# Python Version: 3.9 / 2.7

# Function:
# Mixes bath by moving syringe to zero, to max, then back to start position

# Setup:
# Enter serial ID here
serial_id = '/dev/ttyACM1'

# Enter max rotations from 0 here
maximum_rotations = 6.5

import serial
import time
from reader import Reader

def main():
    # get layer data from layers.csv
    reader = Reader()
    current_syringe_pos = reader.getSyringe_pos()
    max_rotations = maximum_rotations

    #move back to zero
    if (True):

        move = current_syringe_pos * -1

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

    #move to max
    move = max_rotations

    #convert new_syringe_position to string message
    out_str = str(move) + "\n"
    out = bytes(out_str)

    # Send new position to Arduino via serial, wait for move to finish
    ################################################################## 
    messages = 0
    while messages < 1:
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

    #Move back to position
    move = (max_rotations - current_syringe_pos) * -1

    #convert new_syringe_position to string message
    out_str = str(move) + "\n"
    out = bytes(out_str)

    # Send new position to Arduino via serial, wait for move to finish
    ################################################################## 
    messages = 0
    while messages < 1:
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