"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import sys
import os

my_file = open(os.path.join(sys.path[0], "foo.txt"), "r")
my_lines = my_file.readlines()
for line in my_lines:
    print(line)

my_file.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new_file = open(os.path.join(sys.path[0], "bar.txt"), "w")
new_file.write("Super awesome first line\nFollowed by a brilliant second line\nWrapping things up in epic line three.")
new_file.close()