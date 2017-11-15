#!/bin/python3

import json
from requests import get as geturl
import turtle
import os


# NASA Asteroid Data
url = 'https://data.nasa.gov/resource/y77d-th95.json'
response = geturl(url)
result = json.loads(response.text)

#World Map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

#Define the Turtle
plotter = turtle.Turtle()
plotter.hideturtle()
plotter.color('yellow')

#Counters
successcounter = 0
failcounter = 0

for key in result:
    try:
        lat = key['reclat']
        long = key['reclong']
        mass = key['mass']

        plotter.penup()
        plotter.goto(float(long),float(lat))
        
        mass = float(mass)
        if mass > 900:
            plotter.dot(6)
        elif mass > 600:
            plotter.dot(5)
        elif mass > 300:
            plotter.dot(4)
        else:
            plotter.dot(3)

        successcounter += 1
    except KeyError:
        failcounter += 1
    finally:
        os.system('cls')
        print(" " * int((20 - len("Asteroid Plotter")) / 2) + "Asteroid Plotter")
        print("-" * 20)
        print(str(successcounter) + " Successes Plotted")
        print(str(failcounter) + " Missing Data")
        print("-" * 20)





