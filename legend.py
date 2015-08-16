#####################################################################################################
## Script used to shift the legend box
## Run using command: "python3 legend.py inputfile outputfile"
## This program is created on python3 syntax rules
#####################################################################################################import re
import sys
import re

a = sys.argv[1]
e = sys.argv[2]
c = float(input('Enter pixel movement in horizontal direction : '))
d = float(input('Enter pixel movement in vertical direction : '))

while 1:
	try:
		f = open(a,'r')
		break
	except Exception:
		print("File Not Found")
		a = input("Enter file name to read input : ")

output = ''
count = 0
for line in f:
	if re.match('^\[(-|\d|\s|\.)+\]\sCT$',line):
		p = 0.58
		x = []
		x.append(line)
		i = 0
		for line in f:
			x.append(line)
			if re.match('^GR$',line):
				break
			i += 1
			if i == 7:
				if re.match('^cp$',line):
					count += 1
				break
		if count == 2:
			for b in x:
				if re.match('^(\d|\.|-)+\s(\d|\.|-)+\sM$',b):
					y = b.split()
					output += ('%.2f ' % (float(y[0])+c)) + ('%.2f M\n' % (float(y[1])-d)) 
				elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sL$',b):
					y = b.split()
					output += ('%.2f ' % (float(y[0])+c)) + ('%.2f L\n' % (float(y[1])-d))
				elif re.match('^\[(-|\d|\s|\.)+\]\sCT$',b):
					t = re.split('\[|\]|\s',b)
					output += '['+t[1]+' '+t[2]+' '+t[3]+' '+t[4]+(' %.5f' % (float(t[5])+c))+(' %.5f] CT\n' % (float(t[6])-d))
				else:
					output += b
			for line in f:
				if re.match('^(\d|\.|-)+\s(\d|\.|-)+\sM$',line):
					y = line.split()
					output += ('%.2f ' % (float(y[0])+c)) + ('%.2f M\n' % (float(y[1])-d)) 
				elif re.match('^(\d|\.|-)+\s(\d|\.|-)+\sL$',line):
					y = line.split()
					output += ('%.2f ' % (float(y[0])+c)) + ('%.2f L\n' % (float(y[1])-d))
				elif re.match('^\[(-|\d|\s|\.)+\]\sCT$',line):
					t = re.split('\[|\]|\s',line)
					#print(t)
					if float(t[5]) != 0 and float(t[6]) != 0:
						q = next(f)
						if re.match('/Helvetica(\s|\w|\d|.)+$',q):
							output += '['+t[1]+' '+t[2]+' '+t[3]+' '+t[4]+(' %.5f' % (float(t[5])+c/p))+(' %.5f] CT\n' % (float(t[6])-d/p))
							output += q
						else:
							output += '['+t[1]+' '+t[2]+' '+t[3]+' '+t[4]+(' %.5f' % (float(t[5])+c))+(' %.5f] CT\n' % (float(t[6])-d))
							output += q
					else:
						output += line
				else:
					output += line
		else:
			for b in x:
				output += b
	else:
		output += line

f.close()
g = open(e,'w')
g.write(output)
g.close()
