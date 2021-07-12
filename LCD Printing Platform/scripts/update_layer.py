# File name: update_layer.py
# Author: John Jubenville
# Date created: 06/30/2021
# Date last modified: 07/12/2021
# Python Version: 3.9 / 2.7

# Function:
# increases the current layer in temp.csv by 1, updates position

import csv
from reader import Reader

def main():
    # get layer number and position from progress.tmp (change this to command line arg if possible in NanoDLP)
    # get layer data from layers.csv
    reader = Reader()
    current_layer = reader.getCurrent_layer()
    syringe_pos = reader.getSyringe_pos()

    # update progress.tmp
    with open('temp.csv', 'w') as progress_file:
        writer = csv.writer(progress_file)
        writer.writerow([current_layer + 1, syringe_pos])

main()
