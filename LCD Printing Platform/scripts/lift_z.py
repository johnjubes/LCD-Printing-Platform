# File name: lift_z.py
# Author: John Jubenville
# Date created: 06/22/2021
# Date last modified: 07/12/2021
# Python Version: 3.9 / 2.7

# Function:
# lift_z.py is called after a layer is cured
# It lifts the plate by the set lift_distance by returning a line of g-code to NanoDLP

import sys
from reader import Reader

#set lift distance here (mm)
lift_distance = 5.0

def main():
    reader = Reader()

    lift_z_pos = str(reader.getZ_pos() + lift_distance)
    sys.stdout.write('G1 Z' + lift_z_pos)

main()
