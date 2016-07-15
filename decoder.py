import struct
from io import *
import os
import sys
def unpacked_file(filename):
	f=open(filename,'rb')
	in_str=f.read()
	x_in=struct.unpack('>%dH' %(os.path.getsize(filename)/2),in_str)
	counter=0
	char_array=[]

	for i in x_in:
		if(counter%2==0):
			offset=i >> 6
			length=i&0x003f
			#print(offset, end=' ')
			#print (length, end=' ')
			if(offset>0):
				char_array.extend(char_array[offset:length+offset])
			else:
				char_array.extend(char_array[0:length])
		if(counter%2!=0):
			unpacked_char=chr(i)
			char_array.append(unpacked_char)
		counter=counter+1
	print(''.join(char_array))

def main():
	newfile=sys.argv[1]
	unpacked_file('newtest1.bin')

if __name__== '__main__': 
    main()
