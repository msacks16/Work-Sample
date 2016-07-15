#maxwell sacks
#lab 2


import struct
import os
import sys

MAX_SEARCH=1024
MAX_LOOKAHEAD=64

def parsed(filename):
	word_list=[]
	f=open(filename,'rb')
	wholef=f.read() #.strip('\n')
	sent1=list(wholef)
	for i in sent1:
		word_list=word_list+[i]
	return (word_list)

def LZ77_search(search, lookahead):
    ls=len(search)
    lla= len(lookahead)
    if(ls==0):
        return(0,0,lookahead[0])
    if(lla==0):
        return(-1,-1,"")
    best_offset=0
    best_length=0
    buf=search+lookahead
    #print(buf)

    sp=ls

    #print ("search:", search, "lookahead:", lookahead)

    for i in range(0,ls):
        length=0
        while buf[i+length]==buf[sp+length]:
            length+=1
            if sp+length==len(buf):
                length-=1
                break
            if i+length==sp:
            	break
        if length > best_length:
            best_offset=i
            best_length=length
    return (best_offset, best_length, buf[sp+best_length])

def encoding_lz(infile, outfile):

	search_idx=0
	lookahead_idx=0
	input=list(infile)
	while lookahead_idx<len(input):
		search=input[search_idx:lookahead_idx]
		lookahead=input[lookahead_idx:lookahead_idx+MAX_LOOKAHEAD]
		(offset, length, char)=LZ77_search(search,lookahead)
		#print (offset,length,char)
		shifted_offset=offset << 6
		offset_and_length=shifted_offset+length
		ol_bytes= struct.pack(">H", offset_and_length)
		char_byte=struct.pack("B", char)
		outfile.write(ol_bytes)
		outfile.write(char_byte)
		#outfile.write(char)
		lookahead_idx += length+1
		search_idx=lookahead_idx-MAX_SEARCH
		if search_idx<0:
			search_idx=0
    

def unpacked_file(filename):
	f=open(filename,'rb')
	in_str=f.read()
	#
	#i+=3
	counter=0
	script=""
	i=0
	while i<len(in_str):
		(offset_and_length, char) = struct.unpack(">HB", in_str[i:i+3])
		offset=offset_and_length >> 6
		length=offset_and_length-(offset<<6)
		unpacked_char=chr(char)
		if (offset == 0 and length == 0):
			script += unpacked_char
		
		else:
			ol = len(script) - MAX_SEARCH

			if (ol <0):
				ol = offset
			else:
				ol += offset
			for k in range(length):
				script += script[ol+k]
			script += unpacked_char
		i+=3
	return script

def main():
	parsedfile=parsed(sys.argv[1])
	filetobeLZ=sys.argv[2]
	LZfile=open(filetobeLZ,'wb')
	file = encoding_lz(parsedfile, LZfile)
	LZfile.close() 
	unpackLZ = unpacked_file(filetobeLZ)
	fileback=sys.argv[3]
	stringfile=open(fileback,'w')
	stringfile.write(unpackLZ)
    
if __name__== '__main__': 
    main()

## use diff file1 file2 in terminal window