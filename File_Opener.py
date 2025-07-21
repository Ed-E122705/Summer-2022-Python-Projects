# AD1 Systems - File Opener

# This project is a file opener which opens a file based on what kind of file it is. Make sure to add your path

import os

location = input("Location of file: ")
path = 'C:\\Add your filepath here' + str(location)
os.chdir(path)

print("Type of file you want to open?")
print("1. Word document")
print("2. PDF")
print("3. Excel")
print("4. PowerPoint")
print("5. Image\n")
typeoffile = input()

if typeoffile == "1":
    fileopen = input("Index of file: ")
    os.startfile(fileopen + ".docx")

elif typeoffile == "2":
    fileopen1 = input("Index of file: ")
    os.startfile(fileopen1 + ".pdf")

elif typeoffile == "3":
    fileopen2 = input("Index of file: ")
    os.startfile(fileopen2 + ".xlsx")

elif typeoffile == "4":
    fileopen3 = input("Index of file: ")
    os.startfile(fileopen3 + ".pptx")

elif typeoffile == "5":
    fileopen4 = input("Index of file: ")
    os.startfile(fileopen4)

else:
    print("Error. Please try again.")