#!/usr/bin/env python3
# OPS435 - Lab 3
# temp3.py
# Author: Avraham Abel

def square(number):
	return number ** 2

# ~ print(square(5))
# ~ print(square(10))
# ~ print(square(12))

# ~ print(square(square(2)))

def sum_numbers(number1, number2):
	return int(number1) + int(number2)
	
print(square(sum_numbers("2", "2")))
