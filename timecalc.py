#!/usr/bin/python

from platform import python_version
import time

if python_version().split(".")[0] == "2":
	print("Running in Python 2")
	t1 = raw_input("Starting time (hours:minutes): ")
	t2 = raw_input("Ending time (hours:minutes): ")
else:
	print("Running in Python 3")
	t1 = input("Starting time (hours:minutes): ")
	t2 = input("Ending time (hours:minutes): ")

t1h = int(t1.split(":")[0])
t1m = int(t1.split(":")[1])
t2h = int(t2.split(":")[0])
t2m = int(t2.split(":")[1])

hours = t2h - t1h
minutes = t2m - t1m

if minutes < 0:
	hours = hours - 1
	minutes = minutes + 60

print("Total time: " + str(hours) + ":" + str(minutes))
