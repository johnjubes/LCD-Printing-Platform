# File name: init_print.py
# Author: John Jubenville
# Date created: 05/09/2021
# Date last modified: 05/09/2021
# Python Version: 3.9

# Contains the Syringe class, which will be used as the interface for the arduino steppers
# Much still to do, will flesh out more when the arduino arrives

class Syringe:

    def __init__(self):
        # create connection to arduino
        print(self.getStatus())

    def setPosition(self, pos):
        self.position = pos

    def getStatus(self):
        # get status from arduino (moving, not moving, error, etc)
        return 'syringe ready'

    def getPosition(self):
        return self.position

    def moveToPosition(self):
        print('moving syringe to', self.position)
        # call steppers to position
        # while getStatus == moving: wait
        print(self.getStatus())