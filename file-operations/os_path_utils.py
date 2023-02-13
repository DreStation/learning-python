import os
from os import path
import datetime
import time

# Print name of OS
print(os.name)

# Check for item existence
print("Item exists:", str(path.exists("my_file.txt")))
print("Item is a file:", str(path.isfile("my_file.txt")))
print("Item is a directory:", str(path.isdir("file-operations")))

# Get file path
print("Item's path:", path.realpath("my_file.txt"))
print("Item's path and name:", path.split(path.realpath("my_file.txt"))) # Returns a tuple :o

# Get modification time
t = time.ctime(path.getmtime("my_file.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("my_file.txt")))

# Calculate how long ago the file was modified
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("my_file.txt"))
print("It has been", td, "since the file has been modified")
print("or", td.total_seconds(), "seconds")