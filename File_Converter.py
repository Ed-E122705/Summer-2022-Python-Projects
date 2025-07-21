# AD1 Systems - File Converter

# This project helps convert your file from one file format to another

import os

location = input("\nLocation of file: ")
path = 'C:\\Add your filepath here' + str(location)
os.chdir(path)

my_file = input()
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.pdf')