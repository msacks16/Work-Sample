README for lab 2
The way my program works is that I first read in the file through the sys.argv by means of 
entering the file name in the terminal window which reads the file in terms of bytes.  I have 3 arguments you
need to enter in this file.  The first is the text file you want to compressed.  The second is the .bin name you
want to compress the file into for binary and the third is the uncompressing of the file which is a .txt ending
After that my program parses the file and then compresses it using the LZ77 algorithm.  It packs the the offset,
length, and char into a tuple.  After it does this I write it in my out file as bytes.  When I unpack I read
the binary output file and unpack the offset and legnth and then the char.  I get an offset by shifting it
6 spaces to the right and a length by subtracting offset+length-(offset shifted 6 to the left).  Once I get
that I am able to start decoding the binary file back to the txt file.  If the offset and length are 0 I put
the char from the tuple to the end of the string.  If they are not both equal to 0 I find the starting position
and find the length and I start appending each character in the range to the end of the string by means of a for
loop.  Then I return the string and write it back into the .txt file that you named in main.

The entropy results for "lab1_data.txt" was 
The compression I got for alice and wonderland ("alice.txt") was that I turned a 164 KB file into a 115 KB file
thus 1-(115/164)=.2987 so I got about 30% compression for that file.  The entropy was 4.59 for txt and 6.9 for the
bin
The compression I got for Deadend ("deadend.txt") was that I turned a 44 KB file into a 31 KB file
thus 1-(31/44)=.29545 so I got again about 30% compression for that file.  The entropy was 4.675 for txt and 
6.87 for the bin
The compression I got for lab1_data.txt was that I turned a 582 KB file into a 434 KB file
thus 1-(434/582)=.254 so I got again about 25% compression for that file.  The entropy was 4.49 for txt and 6.83 
for the bin
The compression I got for 1M.bin was that I turned a 1 MB file into a 1.6 MB file
thus 1-(1.6/1)=1.2 so I got again about -60% compression for that file. The entropy was 6.25 for txt (decompressed 
file) and 6.76 for the bin.  This was probably due to the randomness of the file and lack of repitition.
My non random non text file compressed about 30% as well.  This result makes sense because it was non random.

Things like zip and gzip do a second pass of compression over the tuples to get almost double the amount
of compression that was achieved in this program.  By doing a second pass you are further decreasing the bytes
and further compressing the files.  This makes it easy to send those file over the internet where you can download
the zip and then unpack it faster when its on your computer instead of unpacking it from the internet.


# Work-Sample
# Work-Sample
# Work-Sample
