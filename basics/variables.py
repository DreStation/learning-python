# Naming convention: snake_case

# Data types
my_int = 5
my_float = 8.8
my_str = "🐍 Sss!"
my_bool = True
my_list = [0, 1, "two", 3.2, False]
my_tuple = (0, 1, 2)
my_dict = {"one" : 1, "two" : 2} # Key : Value

# print(my_int)
# print(my_float)
# print(my_str)
# print(my_bool)
# print(my_list)
# print(my_tuple)
# print(my_dict)

# Reassign from int to string
my_int = "This is a string now"
print(my_int)

# Access lists and tuples with an index
print(my_list[0])
print(my_tuple[1])

# Get items 1-3
print(my_list[1:3])

# Specify step value
print(my_list[1:5:2])

# Reversed list
# :: means unspecified start and end
print(my_list[::-1])

# Access a dictionary with the key
print(my_dict["one"])

# Error: can't concat different types
# print("concat this " + 123)
# Fixed!
print("concat this " + str(123))

# Global vs local var
def my_function():
    # Tell it to affect the var globally
    global my_str
    my_str = "bruh"
    print(my_str)
    
my_function() # "bruh"
print(my_str) # Normally "🐍 Sss!", but now is "bruh"

# Unassigning a variable/deleting
del my_str
print(my_str)