##############################################################################################################
## Aim :- This program aims at scaling a matlab .eps figure(i.e increasing or decreasing its size)
## Run using command : "python3 scale2.py inputfile outputfile"
## Input the file to be scaled , Input the output file name, Input the scale degree
##############################################################################################################
import re
import sys

a = sys.argv[1]
b = sys.argv[2]
c1 = float(input('Enter horizontal dimension in cm : '))*96/2.54		# centimetres to pixels conversion
c2 = float(input('Enter vertical dimension in cm : '))*96/2.54			# as default units is pixels
while 1:
	try:
		f = open(a,'r')
		break
	except Exception:
		print("File Not Found")
		a = input("Enter file name to read input : ")

scaleX = 1
scaleY = 1
output = ''
for line in f:
	if re.match('^\[(-|\d|\s|\.)+\]\sCT$',line):
		x = re.split('\[|\]|\s',line)
		output += '['+x[1]+' '+x[2]+' '+x[3]+' '+x[4]+' '+('%.5f' % (float(x[5])*scaleX))+' '+('%.5f' % (float(x[6])*scaleY))+'] CT\n'
	elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sM$',line):
		x = re.split('\[|\]|\s',line)
		output += ('%.2f' % (float(x[0])*scaleX))+' '+('%.2f' % (float(x[1])*scaleY))+' M\n'
	elif re.match('^%%PageBoundingBox:\s(\d|\.|-)+\s(\d|\.|-)+\s(\d|\.|-)+\s(\d|\.|-)+$',line):
		x = line.split()
		scaleX = c1/float(x[3])
		scaleY = (c2*842/480)/float(x[4])
		output += '%%PageBoundingBox:'+(' %.2f' % (float(x[1])*scaleX))+(' %.2f' % (float(x[2])*scaleY))+(' %.2f' % (float(x[3])*scaleX))+(' %.2f\n' % (float(x[4])*scaleY))
	elif re.match('^/Helvetica\s(\d|\.|-)+\sF$',line):
		x = line.split()
		output += x[0]+(' %.2f' % (float(x[1])*(scaleX+scaleY)/2))+' F\n'
	elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sL$',line):
		x = re.split('\[|\]|\s',line)
		output += ('%.2f' % (float(x[0])*scaleX))+(' %.2f' % (float(x[1])*scaleY))+' L\n'
	else :
		output += line
f.close()
g = open(b,'w')
g.write(output)
g.close()

