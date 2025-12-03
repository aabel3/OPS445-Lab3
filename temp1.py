#!/usr/bin/env python3

def hello():
	print('Hello World!')
	print('Inside a Function')
	
def return_text_value():
	name = 'Terry'
	greeting = 'Good Morning ' + name
	return greeting

text = return_text_value()

print(text)
