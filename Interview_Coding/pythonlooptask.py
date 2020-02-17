#!/usr/bin/env python3 

"""The requirements of the project are as follows: #Create a Python application that will loop between 1 and 100. 
#The numbers are to be printed out alongside their squared value. 
#The app should stop when a squared value of 200 or more is reached. 
#Reconfigure the application to take in a user value to produce squared values up to."""



__appname__ = '[Python Loop Task]'
__author__ = 'Tegan Beale (teganbeale@gmail.com)'
__version__ = 'Feb 2020'

## imports ##
import sys # module to interface our program with the operating system

##constants##

## functions ##
def main(argv):

# creates the loop between 1 and 100
	for k in range(1, 100):
# this finds their square value
		sq = k * k
# making sure loop stops when squared value reaches 200
		if sq < 200: 
# prints them out side by side
			print(k, sq) 

# asking for user input
	f = input("Enter User Value: ")
# turning input string into integer
	f = int(f)
	for k in range(1, 100): 
		sq = k * k 
# now loop will stop when it reaches user input value
		if sq < f: 
			print(k, sq)

if __name__ == "__main__":
	status = main(sys.argv)
	sys.exit(status)	
	

