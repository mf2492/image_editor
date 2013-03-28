# *************************************
# Michelle Fernandez
# 10/25/12
# file: A3.py
#
# This program edits a ppm file.
#***************************************

import color
import os


def main():
    
    greeting()
    image_file = raw_input("Enter name of image file: ")
    infile = inputfile(image_file)
    outputname = raw_input("Enter name of output file: ")
    outfile = outputfile(outputname)
    menu()

    for index in range(1,11):
        print "Do you want [", index,"]? (y/n) ",
        choice = raw_input()
        if (choice == "y"):
            temp_file = open('temp.ppm', 'w')
            readFile(infile, temp_file, index)
            infile = open('temp.ppm', 'r') #change input file to current out.ppm file
            os.rename('temp.ppm', outputname)

    temp_file.close()        
    print outputname, "created"
    

    
def inputfile(image_file):
    infile = open(image_file, "r")
    return infile

def outputfile(outputname):
    outfile = open(outputname, "w")
    return outfile



# Reads and copies a file.[Errno 2] No such file or directory
def readFile(infile, outfile, index):
    type_PPM = infile.readline() #reads PPM type
    dimension = infile.readline() #reads dimension
    max_color = infile.readline() #reads max color


    #Copies specified file into new file
    outfile.write(type_PPM)
    outfile.write(str(dimension))
    outfile.write(str(max_color))


    #determines length of line 
    stringlist = dimension.split()
    length = [int(item) for item in stringlist]
    row = length[0] * 3
    height = int(stringlist[1])

    if row < 3000:
        x = 0
        pixels = infile.read()
        stringlist = pixels.split()
        stringlist = [int(item) for item in stringlist]
        increase = row

        for item in range(height):
            linetoread = stringlist[x:row]
            if index == 1:
                outfile.write(color.grey_scale(linetoread) + '\n')
            elif index == 2:
                outfile.write(color.flip_horizontal(linetoread) + '\n')
            elif index == 3:
                outfile.write(color.negate_red(linetoread) + '\n')
            elif index == 4:
                outfile.write(color.negate_green(linetoread) + '\n')
            elif index == 5:
                outfile.write(color.negate_blue(linetoread) + '\n')
            elif index == 6:
                outfile.write(color.flatten_red(linetoread) + '\n')
            elif index == 7:
                outfile.write(color.flatten_green(linetoread) + '\n')
            elif index == 8:
                outfile.write(color.flatten_blue(linetoread) + '\n')
            elif index == 9:
                outfile.write(color.extreme_contrast(linetoread) + '\n')
            elif index == 10:
                outfile.write(color.random_noise(linetoread, 50) + '\n')
            else:
                print "Invalid choice"
            
       
            x = row
            row = row + increase
    else:
        print "Image too large."
        print "Program aborted."

    infile.close()
    outfile.close()

# Prints menu
def menu():
    print "\nHere are your choices:"
    print "[1] convert to greyscale [2] flip horizontally"
    print "[3] negative of red [4] negative of green [5] negative of blue"
    print "[6] just the reds [7] just the greens [8] just the blues"
    print "[9] extreme contrast [10] add random noise\n"

   

# Prints greeting
def greeting():
    print "Portable Pixmap (PPM) Image Editor!\n"


# Call the main function
main()
