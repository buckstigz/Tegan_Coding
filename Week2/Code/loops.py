# FOR loops in Python
for i in range(5):
	print(i)
# will print 0-4

my_list = [0, 2, "geranimo!", 3.0, True, False]
for k in my_list:
	print(k)
# iterate through list and print them

total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
	total = total + 2
	print(total)

# s will loop through the values of 'summands' ( 5 values in total ) and will print total variable plus 2. This loop ends after 5 values because there are only 5 values in summands!

total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
	total = s + 2
	print(total)

# this s represents the values of summands and increments them by 2 for a total of 5 iterations. 

# WHILE loops in Python
z = 0
while z < 100:
	z = z + 1
	print(z)

a =0 
b = True
while b:

	print("GERANIMO! infinite loop! ctrl+c to stop!")
#ctrl + c to stop!!
