# import os 

# directory = "C:\Users\jakub\Desktop\VÚKOZ\WIP"
# file_name = "PYoutput.txt"

import pyperclip

degree = int(input("Enter degrees"))
minute = int(input("Enter minutes"))
second = int(input("Enter seconds"))

try:
    convert = degree + minute/60 + second/3600
except :
    convert = degree + minute/60


print(convert)


