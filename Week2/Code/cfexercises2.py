# Loops and Conditionals combined

for j in range(12):
	if j % 3 == 0:
		print('hello')

# in a range of 12 (0-11) each value is divided by 3. the number of times that the remainder is '0' is the number of times that hello is printed - 4!

for j in range(15):
	if j % 5 == 3:
		print('hello')
	elif j % 4 == 3:
		print('hello')

#in a range of 15 (0-14) each value is divided by 5 - the number of times that the remainder is 3 will print hello. if this is true then the elif statement is ignored and the loop runs from the beginning. If the remainder is NOT 3 then the elif statement is triggered, if true then prints, if not then loops to beginning with next value. 

z = 0 
while z != 15:
	print('hello')
	z = z + 3

#!= means NOT EQUAL. If z is not equal to 15 then will print hello and then add 3 to z variable. When z becomes equal to 15 then the loop will end.

z = 12
while z < 100:
	if z == 31:
		for k in range(7):
			print('hello')
	elif z == 18:
		print('hello')
	z = z + 1

# whilst z is less than 100 we do this : when z is 31 we print hello 7 times. when z is 18 we print hello ones. at the end of the iteration we add one. prints 8 hellos, obviously.


