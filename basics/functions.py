#
# Function with no args
#
print("\n<Function with no args>")

def func1():
    print("I am a function")

func1() # "I am a function"
print(func1()) # "None" it's trying to print the return value
print(func1) # Prints the function as an object

#
# Functions with args
#
print("\n<Functions with args>")

def func2(arg1, arg2):
    print(arg1, arg2)

def cube(x):
    return x * x * x

func2("ayy", "lmao")
print(cube(2))

#
# Arg has a default value
#
print("\n<Functions with args>")

def power(num, x = 1):
    result = 1

    # For loop
    # for (int i = 0; i < x; i++)
    for i in range(x):
        result = result * num
    return result

print(power(2)) # 2^1
print(power(2, 3)) # 2^3
print(power(x = 3, num = 2)) # 2^3

#
# Function with variable number of args
#
print("\n<Function with variable number of args>")

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(1 + 1 + 1))