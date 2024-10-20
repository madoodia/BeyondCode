# import PySide2 # Qt for Python

import numpy
# import PySide2
import api

counter = 10

def sayHello(msg):
	global counter
	counter -= 1
	print("Your Message: ", msg)
	if(counter > 0):
		sayHello(msg)

x = 5
y = 10
z = x + y

sayHello(z)

# fibonaaci series 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# factorial 5! = 5 * 4 * 3 * 2 * 1 = 120