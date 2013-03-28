# *************************************
# Michelle Fernandez
# 10/25/12
# file: color.py
#
# This program contains the functions that edits
# the ppm images.
#***************************************

import random

# Negates the red number of each pixel.
def negate_red(linetoread):
    for index in range(0, len(linetoread), 3):
        linetoread[index] = 255- int(linetoread[index])
    return ' '.join(str(x) for x in linetoread)

    
# Negates the green number of each pixel.    
def negate_green(linetoread):
    for index in range(1, len(linetoread), 3):
        linetoread[index] = 255- int(linetoread[index])
    return ' '.join(str(x) for x in linetoread)

    
# Negates the blue number of each pixel.
def negate_blue(linetoread):
    for index in range(2, len(linetoread), 3):
        linetoread[index] = 255- int(linetoread[index])
    return ' '.join(str(x) for x in linetoread)


# Sets each pixel to the average of the three
def grey_scale(linetoread):
    i = 0
    while i < len(linetoread):
        total = (linetoread[i] + linetoread[i+1] + linetoread[i+2]) / 3
        linetoread[i] = total #R value
        linetoread[i+1] = total #G value
        linetoread[i+2] = total #B value
        i = i + 3
    return ' '.join(str(x) for x in linetoread)


# Flips each row horizontally
def flip_horizontal(linetoread):
    i = 0
    group = []
    while i < len(linetoread):
        group.append([linetoread[i],  linetoread[i+1], linetoread[i+2]])
        i = i + 3
    group.reverse()
    j = 0
    while j < (len(linetoread)/3):
        group[j] = ' '.join(str(x) for x in group[j])
        j = j + 1

    group =  ' '.join(str(x) for x in group)
    return group


# Sets the red value to zero
def flatten_red(linetoread):
    for index in range(0, len(linetoread), 3):
        linetoread[index] = 0
    return ' '.join(str(x) for x in linetoread)


# Sets the green value to zero
def flatten_green(linetoread):
    for index in range(1, len(linetoread), 3):
        linetoread[index] = 0
    return ' '.join(str(x) for x in linetoread)


# Sets the blue value to zero
def flatten_blue(linetoread):
    for index in range(2, len(linetoread), 3):
        linetoread[index] = 0
    return ' '.join(str(x) for x in linetoread)


# Sets each color number either to the highest color value or to zero.
def extreme_contrast(linetoread):
    for index in range(1, len(linetoread)):
        if linetoread[index] > 255/2:
            linetoread[index] = 255
        elif linetoread[index] < 255/2:
            linetoread[index] = 0
    return ' '.join(str(x) for x in linetoread)


# Randomly adds or subtracts a random number from the color value.
def random_noise(linetoread, ranrange):
    for index in range(1, len(linetoread)):
        add_subtract = random.randint(0,1)
        change = random.randint(0, ranrange)
        if add_subtract == 0 and (int(linetoread[index]) - change >= 0):
            linetoread[index] = int(linetoread[index]) - change
        elif add_subtract == 0 and (int(linetoread[index]) - change < 0):
            linetoread[index] = 0
        elif add_subtract == 1 and (int(linetoread[index]) + change <= 255): 
            linetoread[index] = int(linetoread[index]) + change
        else:
            linetoread[index] = 255
    return ' '.join(str(x) for x in linetoread)
