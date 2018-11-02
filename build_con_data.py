from functions.constants import *
import os

directory = os.fsencode(con_path)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.system("./functions/increase_picture.py " + con_path + filename)
