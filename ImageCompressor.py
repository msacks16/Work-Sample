#CMiC Image Compressor Starter file
#first some imports
import sys
import scipy
import scipy.ndimage
import numpy as np
import PIL
import pywt
import argparse

import operator
from heapq import merge
import struct
import json
import hashlib
#wrapper for showing np.array() as an image
def show(image):
	scipy.misc.toimage(image).show()

#open the image and take the 2D DWT
#After that, it's up to you!
class Counter(dict):
	def __missing__(self,key):
		return 0

def parsed(lister):
	dictionary=Counter()
	for i in lister:
		dictionary[int(i)]+=1
	return (dictionary.items())

def huff(lst, accumulator, code):
	if type(lst) is int :
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

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input_image")
	parser.add_argument("output_file")
	parser.add_argument("--wavelet", help="wavelet name to use. Default=haar", default="haar")
	parser.add_argument("--quantize", help="quantization level to use. Default=4", type=int, default=1)
	args = parser.parse_args()

	input_file_name = args.input_image
	output_file_name=args.output_file
	try:
		im = scipy.ndimage.imread(input_file_name, flatten=True, mode="L")
		print ("Attempting to open %s..." % input_file_name)
	except:
		print ("Unable to open input image. Qutting.")
		quit()
	#show(im)
	#get height and width
	(height, width) = im.shape
	wavelet = args.wavelet
	q = args.quantize
	
	LL, (LH, HL, HH) = pywt.dwt2(im, wavelet, mode='periodization')
	
	'''the following block of code will let you look at the decomposed image. Uncomment it if you'd like
	'''
	dwt = np.zeros((height, width))
	dwt[int(0):int(height/2), int(0):int(width/2)] = LL
	dwt[int(height/2):,int(0):int(width/2)] = HL
	dwt[int(0):int(height/2), int(width/2):] = LH
	dwt[int(height/2):,int(width/2):] = HH
	#show(dwt)
	#print(LL)
	flat_LL=LL.flatten()
	flat_LL=np.round(flat_LL)
	#print(len(flat_LL))
	LLq=np.insert(flat_LL, 0, 0)
	LLq=np.diff(LLq)
	
	#quantize
	HLq=np.round(HL/q)
	LHq=np.round(LH/q)
	HHq=np.round(HH/q)
	#type
	LLq=LLq.astype(int)
	HLq=HLq.astype(int)
	LHq=LHq.astype(int)
	HHq=HHq.astype(int)
	#height
	#len_LLq=len(LLq)
	#len_HLq=len(HLq.tolist())
	#len_LHq=len(LHq.tolist())
	#len_HHq=len(HHq.tolist())
	#height=len_HLq*2
	#width=len(HHq[0])*2
	#print(height)
	#print(width)
	#print(4*((.5*height)*(.5*width)))
	#width

	#flatten
	HLq=HLq.flatten()
	LHq=LHq.flatten()
	HHq=HHq.flatten()
	#turn into list
	LLq=LLq.tolist()
	HLq=HLq.tolist()
	LHq=LHq.tolist()
	HHq=HHq.tolist()
	#final list of LL HL LH HH
	finalLLHH=[]
	finalLLHH.extend(LLq)
	finalLLHH.extend(LHq)
	finalLLHH.extend(HLq)
	finalLLHH.extend(HHq)

	
	#lenght
	length=len(finalLLHH)
	#print("this is length: ", length)
	#Huffman Part
	#print(finalLLHH)
	filedict=parsed(finalLLHH)
	#print(filedict)
	huff_dict=getAlpha(filedict)
	#print(huff_dict)
	encodedstr=""
	for ele in finalLLHH:
		encodedstr+=huff_dict[ele]
	adder=8-(len(encodedstr)%8)
	for i in range(0,adder):
		encodedstr+="0"
	lengthadded=len(encodedstr)
	#print(lengthadded)
	binary=b''
	for i in range(0,lengthadded,8):
		binary+=char2bin(encodedstr[i:i+8])
	#print(len(binary)*8)
	#get the file size=file.tell()
	#rewind it
	#hashlib.md5(input file data).hexdigest()
	jsonhuff=json.dumps(huff_dict)
	dictionary={'version': 'CMiCv1', 'width': width, 'height': height, 'wavelet': wavelet,'q': q}
	jsondict=json.dumps(dictionary)
	#open a new compressed file
	mapfile=open(output_file_name,'wb')
	#write the header which is json.dumps(dictionary) +new line
	mapfile.write(jsondict.encode())
	mapfile.write('\n'.encode())
	#write the json.dumps(huff_dict) + new line
	mapfile.write(jsonhuff.encode())
	mapfile.write('\n'.encode())
	#write the binary into the bin file
	mapfile.write(binary)
if __name__ == '__main__':
	main()