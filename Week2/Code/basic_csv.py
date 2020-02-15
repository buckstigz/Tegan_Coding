import csv

# Read a file containing:
# 'Species', 'Infraorder', 'Family', 'Distribution', 'Body Mass Male (KG)'
f = open('../../../Test_Files/Data/testcsv.csv', 'r')

csvread = csv.reader(f)
temp = []
for row in csvread:
	temp.append(tuple(row))
	print(row)
	print("The species is", row[0])

f.close()

# Write a file containing only species name and body mass
f = open('../../../Test_Files/Data/testcsv.csv', 'r')
g = open('../Sandbox/bodymass.csv', 'w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
	print(row)
	csvwrite.writerow([row[0], row[4]])

f.close()
g.close()
