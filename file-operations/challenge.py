# Create a folder
# Inside, create a txt file containing the byte count
# and the name of each file in the folder

import os
from os import path

# Set file-operations as the current directory
# Otherwise it uses the root directory and breaks things
os.chdir("file-operations")

# Create the folder if it doesn't exist yet
if path.exists("challenge") == False:
   os.mkdir("challenge")

with open("challenge/result.txt", "w+") as file:
    # Get list of files
    files = filter(os.path.isfile, os.listdir(os.curdir))

    # Get total byte count
    bytes = 0
    for f in files:
        bytes += os.stat(f).st_size
    file.write("Total byte count: " + str(bytes) + "\n")

    # Write file names
    file.write("Files here:\n")
    files = filter(os.path.isfile, os.listdir(os.curdir)) # Need to get a ref to the files again?
    [file.write(f + "\n") for f in files] # Short hand list loop