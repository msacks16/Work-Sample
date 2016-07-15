import operator
from heapq import merge
import struct
import json
import hashlib
import sys
#code is data structure
#accumulator is a 1 or 0
#lst is the list

class Counter(dict):
	def __missing__(self,key):
		return 0

def parsed(filename):
	dictionary=Counter()
	f=open(filename,'r')
	wholef=f.read()
	for i in wholef:
		dictionary[i]+=1
	f.close()
	return (dictionary.items())

def huff(lst, accumulator, code):
	if len(lst)==1:
		code.append( (lst,accumulator) )
	else:
		left=huff(lst[0], accumulator+"0", code)
		right=huff(lst[1], accumulator+"1", code)

def getAlpha(items):
	lst= sorted(items, key=lambda y: y[1])
	while len(lst) > 1:
		z = lst[0]
		y = lst[1]
		value = z[1] + y[1]
		key = [z[0], y[0]]
		lst=lst[2:]
		lst.append([key,value])

		lst = sorted(lst, key=lambda y: y[1])
	tree=lst[0][0]
		#print(lst)
	code =[]
	huff(tree,"", code)
		#turn our final list into a dict so we can use it as lookup table
	return(dict(code))

def char2bin(input):
	binary=b''
	for i in range(0, int(len(input)/8)):
		bits=input[i*8:i*8+8]
		b=0
		powers=list(range(0,8))
		powers.reverse()
		for i in range(len(bits)):
			b+=int(int(bits[i])*pow(2,powers[i]))
		binary+=struct.pack("B",b)
	return binary

def dict2binary(diction):
    binary =' '.join(format(ord(letter), 'b') for letter in diction)
    return binary

#def decoder(filename, filebin):
#	encodedfile=open(filename,'r')
#	binfile=open(filebin,'rb')
#	dictionary=json.loads(encodedfile.readline())
#	huff_dict=json.loads(encodedfile.readline())
#	binary=binfile.read()
#	for i in binary:


def main():

	thefile=sys.argv[1]
	filedict=parsed(thefile)
	print(filedict)
	huff_dict=getAlpha(filedict)
	print(huff_dict)
	encodedstr=""
	alice=open(thefile, 'rb')
	for char in alice.read():
		encodedstr+=huff_dict[chr(char)]
	adder=8-(len(encodedstr)%8)
	for i in range(0,adder):
		encodedstr+="0"
	lengthadded=len(encodedstr)
	print(lengthadded)
	binary=b''
	for i in range(0,lengthadded,8):
		binary+=char2bin(encodedstr[i:i+8])
	print(len(binary)*8)
	#get the file size=file.tell()
	alicesize=alice.tell()
	alice.seek(0)
	print(alicesize)
	#rewind it
	#hashlib.md5(input file data).hexdigest()
	md5input=hashlib.md5()
	md5input.update(alice.read())
	hashcode=md5input.hexdigest()
	jsonhuff=json.dumps(huff_dict)
	dictionary={'size': alicesize, 'hash': hashcode}
	jsondict=json.dumps(dictionary)
	#open a new compressed file
	mapfile=open(sys.argv[2],'wb')
	#write the header which is json.dumps(dictionary) +new line
	mapfile.write(jsondict.encode())
	mapfile.write('\n'.encode())
	#write the json.dumps(huff_dict) + new line
	mapfile.write(jsonhuff.encode())
	mapfile.write('\n'.encode())
	#write the binary into the bin file
	mapfile.write(binary)
	#decoder could be in seperate file json.loads(dictionary)
	#the output will be a python dictionary
	#reverse keys and values in huff dict(look up on line)
	#read in the binary
	#undo char2bin
	#string of 0 and 1or an array of 0, 1
	#for loop first pull out a 1 or 0 and look to see if in dict
	#if not you pull out 2, then 3, then 4, ...
	#when hits the file length end so 0's dont show up
if __name__== '__main__': 
    main()