#!/usr/bin/python

while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except NameError:
		print("Oops! That was no valid number. Try again...")

