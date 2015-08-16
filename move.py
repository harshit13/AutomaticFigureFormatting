#####################################################################################################
## Script used to shift and read all text alongwith their coordiantes
## Run using command: "python3 move.py
## Then enter your file name:
## This program is created on python3 syntax rules
#####################################################################################################
import re
import sys
z = sys.argv[1]
e = sys.argv[2]
while 1:
	try:	
		f = open(z,"r")
		break
	except Exception:
		print("File Not Found !!!!!!")
		z = input('Enter file name to read : ')

arr = []

for line in f:
	"""
	if re.match('^%%BoundingBox:(\s|\d)+$',line):
		print(line[2:])
		"""
	if re.match('^\[(-|\d|\s|\.)+\]\sCT$',line):
		y = line.rstrip('\n').split()
		k = 0
		for line in f:
			k += 1
			if re.match('^\((.|\s)+\).*$',line):
				a = re.split('\(|\)',line)
				arr.append([a[1],y[4],y[5].rstrip(']')])
				break
			elif k == 8:
				break
f.close()
f = open(z,"r")
f_string = ''
for line in f:
	f_string += line
f.close()

while 1:
	print('\nPress 1 : View All TEXT alongwith the coordinates associated with them.')
	print('Press 2 : Search a TEXT alongwith the coordinates associated with it.')
	print('Press 3 : Translate a text.')
	print('Press 4 : Exit. Saving Changes')
	print('Press 5 : Exit. Without Saving Changes')

	x = int(input('Enter Your Choice : '))
	if x == 1:
		print("S.no\tText\tXlevel\tYlevel")
		for i,a in enumerate(arr):
			print(str(i+1)+". "+str(a))
		print('\n')
	elif x == 2:
		k = True
		y = input('Enter Text to search : ')
		for i,a in enumerate(arr):
			if re.match(y.rstrip('\n'),a[0]):
				if k:
					print("S.no\tText\tXlevel\tYlevel")
					k = False
				print(str(i+1)+". "+str(a))
	elif x == 3:
		print("S.no\tText\tXlevel\tYlevel")
		for i,a in enumerate(arr):
			print(str(i+1)+". "+str(a))
		print('\n')
		y = list(map(int,input('Enter S.no/S.nos of text to move : ').split()))
		a = float(input('Enter x amount to move : '))
		b = float(input('Enter y amount to move : '))
		for v in y:
			p = float(arr[v-1][1]) + a
			q = float(arr[v-1][2]) - b
			#print(p,q)
			
			f_s = f_string.split('\n')
			final = ''
			for li in f_s:
				if re.match('^\[(-|\d|\s|\.)+\]\sCT$',li):
					t = re.split('\[|\]|\s',li)
					if t[5] == arr[v-1][1] and t[6] == arr[v-1][2]:
						li = '['+t[1]+' '+t[2]+' '+t[3]+' '+t[4]+(' %.5f' % p)+(' %.5f' % q)+'] CT'
				final = final + li + '\n'								
			f_string = final

			arr[v-1][1] = str(p)
			arr[v-1][2] = str(q)
		print('Shifted')
	elif x == 4:
		g = open(e,"w")
		g.write(f_string)
		g.close()	
		print('ThankYou for Using..')
		break
	elif x == 5:
		print('ThankYou for Using..')
		break
	else:
		print('!!!!! Wrong input try again !!!!!')