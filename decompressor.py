import struct
import json
import sys
import hashlib

def main():
	input_file=open(sys.argv[1], "rb")
	header=json.loads(input_file.readline().decode())
	#print (header)

	huffman_code=json.loads(input_file.readline().decode())
	#print(huffman_code)
	decode_dict={v : k.encode() for k, v in huffman_code.items()}
	binary_data= input_file.read()
	binary_str=""
	for byte in binary_data:
		binary_str+= format(byte,'08b')
	decoded_data=b""
	while len(decoded_data) != header['size']:
		sub_str=""
		i=0
		while sub_str not in decode_dict:
			sub_str=binary_str[0:i]
			i+=1
		#print(type(decoded_data))
		decoded_data+=decode_dict[sub_str]
		binary_str=binary_str[i-1:]
	#print(hashlib.md5(decoded_data).hexdigest())
	if hashlib.md5(decoded_data).hexdigest() == header['hash']:
		f=open(sys.argv[2], 'wb')
		f.write(decoded_data)
		f.close()
		print ("MD5 hash matched.") 
		#wrote %i bytes to %s" % (header['size'], header['hash'])
	else:
		print ("MD5 mismatched.")

if __name__ == '__main__':
	main()