# QN 2
import math
# create list to hold the values 
values = []
# input the value of length and height
Length_of_base = float(input('Enter the length:'))
Height_of_parallelogram = float(input('Enter the height'))
# put the values in the list
values.append(Length_of_base)
values.append(Height_of_parallelogram)
# output the value
print(math.prod(values))