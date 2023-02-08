# Only two types of loops in Python :o

def main():
    x = 0

    # Loop until reach 5
    while(x < 5):
        print(x)
        x = x + 1 # Not x++

    # Loop thru specified range
    for x in range(5, 10):
        print(x)

    # Loop thru list
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # Get the index as well
    for i,d in enumerate(days):
        print(i, d)

# Run main()
if __name__ == "__main__":
    main()