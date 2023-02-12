# "w" means write
# "+" means create file if it doesn't already exist
# The contents will be overriden
my_file = open("my_file.txt", "w+")

for i in range(4):
    my_file.write("Some text 1234\n")

# "a" means append
# my_file = open("my_file.txt", "a+")

my_file = open("my_file.txt", "r")

# Check if it opened correctly
if my_file.mode == 'r':
    # Normal read
    # contents = my_file.read()
    # print(contents)
    
    # Get by line
    contents = my_file.readlines()
    for i, line in enumerate(contents):
        print(i, line)

my_file.close()