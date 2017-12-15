"""
File-in-a-Folder Destroyer
Part 1 of computer_class.mover

Licensed under the Creative Commons Attribution-ShareAlike 4.0 International

By: H. Kamran (@hkamran80)
"""

import os
import sys

loc_files = []

class contents:
  path = str(os.getcwd()) + "/"
  directories = next(os.walk(path))[1]

contents = contents()

answers = ["y", "n"]

print(contents.directories)
to_destroy = str(input("Select a folder: "))
if to_destroy.lower() not in contents.directories or to_destroy.lower() == ".." or to_destroy.lower() == ".":
    print("")
while to_destroy.lower() not in contents.directories or to_destroy.lower() == ".." or to_destroy.lower() == ".":
    print("Try again.")
    print(contents.directories)
    to_destroy = str(input("Select a folder: "))
    print(" ")

print("Are you sure you want to delete the contents of the folder:" + to_destroy + "?")
print("Y: Yes, N: No, S: Show Directory")
confirmation = str(input("Y/N/S: "))
if confirmation.lower() == "s":
    path = str(contents.path) + to_destroy + "/"
    destruction_location = next(os.walk(path))[2]
    print(destruction_location)
if confirmation.lower() not in answers:
    print("")
while confirmation.lower() not in answers:
    print("Try again.")
    print("Are you sure you want to delete the contents of the folder:" + to_destroy + "?")
    confirmation = str(input("Y/N: "))
    print(" ")

if confirmation.lower() == "y":
    path = str(contents.path) + to_destroy + "/"
    loc_files = next(os.walk(path))[2]
    loc_len = len(loc_files)
    print(loc_files)
    print(loc_len)
    for filename in loc_files:
        os.remove(path + filename)
    loc_files = []
    print(loc_files)
    print(len(loc_files))
elif confirmation.lower() == "n":
    print("Operation deletion canceled.")
    sys.exit()
