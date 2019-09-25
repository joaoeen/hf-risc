import os
# Removes the file ifit already exists
try:
	os.remove("RAM_DATA.vhd") 
except:
	print("No file found")

def create_mem (data):
	j=0
	num_bytes = 0
	for x in data:
		x = x.replace('"','')
		x = x.replace(' ','')
		for i in range(1,len(x),2):
			bin = "{0:08b}".format(int(x[-(i+2):-i], 16))
			num_bytes = num_bytes + 1
			if j == 0:
				f.write("\"")
			f.write(bin + ",")
			if j > 7:
				f.write("\"&\n")
				j = 0
			else:
				j = j + 1
				
	if num_bytes < 2048:
		for i in range(num_bytes, 2048):
			num_bytes = num_bytes + 1
			if j == 0:
				f.write("\"")
			f.write("00000000" + ",")
			if j > 7:
				f.write("\"&\n")
				j = 0
			else:
				j = j + 1
	print(num_bytes)
	if j != 0 :
		f.write("\"")
	f.write(";\n\n\n")


f = open("RAM_DATA.vhd", "w+")
f.write("-- This file is automatically generate and will be overwriten the next time the script runs\n\n\n\n\n")
f.write("library ieee;\nuse ieee.std_logic_1164.all;\n\npackage RAM_DATA is\n\n")


#Create mem constant 0
f.write("constant RAM0 : string := ")
data_file = open("RAM0.txt", "r")
data = data_file.readlines()
create_mem (data)
data_file.close()

#Create mem constant 1
f.write("constant RAM1 : string := ")
data_file = open("RAM1.txt", "r")
data = data_file.readlines()
create_mem (data)
data_file.close()

#Create mem constant 2
f.write("constant RAM2 : string := ")
data_file = open("RAM2.txt", "r")
data = data_file.readlines()
create_mem (data)
data_file.close()

#Create mem constant 3
f.write("constant RAM3 : string := ")
data_file = open("RAM3.txt", "r")
data = data_file.readlines()
create_mem (data)
data_file.close()

f.write("\n\nend package RAM_DATA;")

f.close()