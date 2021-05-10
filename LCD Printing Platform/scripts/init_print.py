# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 05/09/2021
# Python Version: 3.9

# init_print.py is called by NanoDLP at the start of each print
# It checks that layers.csv exists and is properly formatted, creates the temporary file temp.csv
# which stores the layer number and the syringe stepper position, checks that the arduino is connected,
# and sets the arduino position to 0.

# To Do:
#   check that layers.csv is formatted correctly
#   check arduino connection
#   send position 0 to arduino

import pandas as pd
import csv
from syringe_class import Syringe

def main():
    # check if layers.csv exists and is formatted correctly
    layers_data = pd.read_csv('../layer_profiles/test_layers.csv', sep=',').values

    # create progress.csv with layer number(0) and last syringe position(0)
    with open('temp.csv', 'w', newline='') as progress_file:
        writer = csv.writer(progress_file)
        writer.writerow([0, 0.0])

    # check if arduino is connected, move steppers to zero
    syringe = Syringe()
    syringe.setPosition(0.0)
    syringe.moveToPosition()

main()