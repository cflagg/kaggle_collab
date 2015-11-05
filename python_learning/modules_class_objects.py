# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 09:45:56 2015

@author: cflagg

Modules, Classes, Objects
http://learnpythonthehardway.org/book/ex40.html
"""

# modules are like dictionaries
# dictionaries: get X from Y, a simple index list or 'table'
# in other words, a key:value pair
dict = {'apple' : "I AM A FRUIT", 'tomato' : "I AM ALSO A FRUIT", "carrot" : "I AM A VEGETABLE"}

# modules: files with functions and variables in it
# can be imported into another file whereby you access
# the functions or variables with the . dot operator

import turtle

# call up a screen to draw on
wn = turtle.Screen()

# define two objects, alex and tess, that can draw different patterns
alex = turtle.Turtle() # alex inherits functions from Turtle, it can change color, move, and loop
alex.color('green') # make alex green
alex.shape('circle')
tess = turtle.Turtle() 
tess.color('red') # make tess red

tess.forward(80)             # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)               # Complete the triangle

tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin

alex.forward(50)             # Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick() # make it so user can close screen by clicking the "X" 

