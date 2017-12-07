# Weather App (Python2)

from Tkinter import *
import webbrowser
import urllib2
import json
import sys

key = '' # Put your Weather Underground API key here

state_intials = raw_input('What is the intitals of the state you want to get weather for? ')
city = raw_input('City name? ')

# JSON Parsing
json_data = urllib2.urlopen('http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/%s/%s.json' % (state_intials, city))

json_read = json_data.read()
data = json.loads(json_read)

city = data['location']['city']
state = data['location']['state']

f_temp = data['current_observation']['temp_f']

f_high = 50
f_low = 42.5

# GUI
root = Tk()

tempy = StringVar()
loce = StringVar()
hi = StringVar()
lo = StringVar()

loc = Label(root, textvariable=loce)
blanky = Label(root, text="-----------------------")
temp = Label(root, textvariable=tempy)
high = Label(root, textvariable=hi)
low = Label(root, textvariable=lo)

loce.set(city + ', ' + state)
tempy.set("Current: %s*F" % (f_temp))
hi.set("High: %s*F" % (f_high))
lo.set("Low: %s*F" % (f_low))

loc.pack()
blanky.pack()
temp.pack()
high.pack()
low.pack()

root.title("Weathery")
root.resizable(width=False, height=False)
root.geometry('125x100')
root.mainloop()
