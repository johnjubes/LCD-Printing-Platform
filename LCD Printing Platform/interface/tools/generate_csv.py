import csv

#quick tool for making test_layers.csv


def get_input():

    #enter layer height and print height in mm here
    layer_height = .1
    print_height = 5.0

    return layer_height, print_height

def main():

    layer_height, print_height = get_input()

    number_of_layers = print_height / layer_height

    f = open('layers.csv', 'w')
    f.write("Layer #,Z Axis Value(mm),Syringe Pos(rotations),Exposure(sec)\n")
    f.close
    f = open('layers.csv', 'a')

    z_pos = 0.0
    syringe_pos = 0.0
    exposure = -1.1
    for layer in range(int(number_of_layers)):
        z_pos += layer_height
        z_formatted = "{:.3f}".format(z_pos)
        row = str(layer+1) + ',' + z_formatted + ',' + str(syringe_pos) + ',' + str(exposure) + '\n'
        f.write(row)
    f.write(row)


main()
