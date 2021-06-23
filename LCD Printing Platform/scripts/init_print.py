# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 06/23/2021
# Python Version: 3.9 / 2.7

# Function:
# init_print.py is called by NanoDLP at the start of each print
# It creates the temporary file temp.csv which stores the layer number and the syringe stepper position, and checks that the arduino is connected

# Setup:
# The serial port connection ID is different for each usb slot on the Raspberry pi, the proper port ID must be used to enable serial communication.
# A list of connected devices can be found by using the 'ls /dev/tty*' terminal command, it is likely called '/dev/ttyACM1' or '/dev/ttyACM0'
# Enter the correct ID here:
serial_id = '/dev/ttyACM1'

import csv
import serial
import time

def main():
    # create progress.csv with layer number(0) and last syringe position(0.0)
    with open('temp.csv', 'w') as progress_file:
        writer = csv.writer(progress_file)
        writer.writerow([0, 0.0])

    #Check arduino connection (will throw error if not connected)
    messages = 0
    while messages < 2:
        ser = serial.Serial(serial_id, 9600, timeout = 1)
        ser.flush()

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
        messages = messages + 1
        time.sleep(1)

main()
