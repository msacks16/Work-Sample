README for lab 1
The way my program works is that I first read in the file through a File Input Stream by means of 
entering the file name in the terminal window which reads the file in terms of bytes.  I then add each 
byte type casted as a char to an array list of characters.  Next I close the File Input Stream and 
run my function histogram.  This function takes one arguement which is an array list and returns 
a string.  First I run a for each loop through each element in the array list of characters.  
In each run I first convert the character into a string so that I can account for non printable characters.  
The next part of the run runs each String through an if statement which checks to see if the key was already put 
into the hashmap which is a private variable atop my program.  If it is the first time the key was seen it puts the 
new key into the hash map, if it is not it updates the count of the key by adding one to the previous
number of times the String was seen.  To print my hash map in a readable way, I run another for each
loop through the finished hash table and so that I can print the hash table as one giant string.  The
next function that I created was the calcEntropy that takes in one arguement in the form of a
hash map.  The function returns a double which should be the calculated the entropy.  In this
function I created an iterator that would run through the entry set of the hash map by means of
a while loop.  The loop will run while the iterator has a next.  I then had to get the value
of each map entry that the iterator found next and add it to the total sum of entropy which
the varible is titled totentropy.  I was able to use the Math.log to take the log-base-2 because
it was already built into the java library.  This program multiplied the totEntropy by -1 to
make the entropy positive at the end which can be found in the equation given in lab 1.  Thus
a histogram that turned non printable characters into the hexidecimal equivalent and kept the
count of each character and a function that calculated the entropy was achieved.

The entropy results for "lab1_data.txt" was 4.4934
The entropy results for "dummy.txt" was 7.9981

There was more entropy in the file that I made that was random.  This was expected because
there shoud be more repetition in the "lab1_data.txt file"
# Work-Sample
# Work-Sample
