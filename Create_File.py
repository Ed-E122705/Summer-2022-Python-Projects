# AD1 Systems - File Creater

# This project helps create a new file to your system

import os

location = input("Place where new file must be placed in: ")
path = 'C:\\Add your filepath here' + str(location)
os.chdir(path)

index = input("Index of new file: ")

f = open(str(index), "x")