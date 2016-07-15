README for lab 3
The way my program works is that I first read in the file through the sys.argv by means of 
entering the file name in the terminal window which reads the file in terms of bytes.  I have 2 arguments you
need to enter in this file.  The first is the text file you want to compressed.  The second is the .txt name you
want add the json string of the huffman code and dictionary too and the compressing of the file 
which is in binary.  After that my program parses the file and then compresses it using the huffman algorithm.  
It gets the huffman tree by turning an ordered list to a tree list.  After it does this I run the tree through
my accumulator file which gives each character a prefix code.  This is all done in strings types at first.
Once I get the huffman code dictionary of character:binary string representation.  I run the file again through
my huffman code dictionary to get each characters corresponding binary string in the variable encodedstr.  Once I
have my encodedstr value I add as many 0's to the end of the string so it is divisable by eight and then I run 
the function char2bin to convert these binary strings to actual binary code. The decoder frist reads the file into
binary then it loads the header then dictionary then binary data.  It then adds the binary data to a byte array
then it writes the data into an out file.  This then checks to see if the hash is equal to the hash of the encoded
file.

The compression results for Lab 2 was 
The compression I got for alice and wonderland ("alice.txt") was that I turned a 164 KB file into a 115 KB file
thus 1-(115/164)=.2987 so I got about 30% compression for that file.  The entropy was 4.59 for txt and 6.9 for the
bin

The compression I got for Deadend ("deadend.txt") was that I turned a 44 KB file into a 31 KB file
thus 1-(31/44)=.29545 so I got again about 30% compression for that file.  The entropy was 4.675 for txt and 
6.87 for the bin

The compression results for Lab 3 was
The compression I got for alice and wonderland ("alice.txt") was that I turned a 164 KB file into a 95 KB file
thus 1-(95/164)=.4207 so I got about 42% compression for that file.  

The compression I got for Deadend ("deadend.txt") was that I turned a 44 KB file into a 26 KB file
thus 1-(26/44)=.40909 so I got again about 40% compression for that file.
