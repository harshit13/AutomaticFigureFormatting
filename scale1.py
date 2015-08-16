##############################################################################################################
## Aim :- This program aims at scaling a matlab .eps figure(i.e increasing or decreasing its size)
## Run using command : "python3 scale1.py inputfile outputfile"
## Input the file to be scaled , Input the output file name, Input the scale degree
##############################################################################################################
import re
import sys

a = sys.argv[1]
b = sys.argv[2]
c = float(input('Enter scale amount : '))
while 1:
	try:
		f = open(a,'r')
		break
	except Exception:
		print("File Not Found")
		a = input("Enter file name to read input : ")

scale = c
output = ''
for line in f:
	if re.match('^\[(-|\d|\s|\.)+\]\sCT$',line):
		x = re.split('\[|\]|\s',line)
		output += '['+x[1]+' '+x[2]+' '+x[3]+' '+x[4]+' '+('%.5f' % (float(x[5])*scale))+' '+('%.5f' % (float(x[6])*scale))+'] CT\n'
	elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sM$',line):
		x = re.split('\[|\]|\s',line)
		output += ('%.2f' % (float(x[0])*scale))+' '+('%.2f' % (float(x[1])*scale))+' M\n'
	elif re.match('^%%PageBoundingBox:\s(\d|\.|-)+\s(\d|\.|-)+\s(\d|\.|-)+\s(\d|\.|-)+$',line):
		x = line.split()
		output += '%%PageBoundingBox:'+(' %.2f' % (float(x[1])*scale))+(' %.2f' % (float(x[2])*scale))+(' %.2f' % (float(x[3])*scale))+(' %.2f\n' % (float(x[4])*scale))
	elif re.match('^/Helvetica\s(\d|\.|-)+\sF$',line):
		x = line.split()
		output += x[0]+(' %.2f' % (float(x[1])*scale))+' F\n'
	elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sL$',line):
		x = re.split('\[|\]|\s',line)
		output += ('%.2f' % (float(x[0])*scale))+' '+('%.2f' % (float(x[1])*scale))+' L\n'
	else :
		output += line
f.close()
g = open(b,'w')
g.write(output)
g.close()
