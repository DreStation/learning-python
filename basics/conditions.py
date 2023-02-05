def main():
    x, y = 2, 5

    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x and y are equal"
    else:
        result = "x is greater than y"
    print(result)

    #
    # One liner
    #
    x = 10
    result = "x is less than y" if x < y else "x is greater than or equal to y"
    print(result)
    
    #
    # Match case (switch)
    #
    value = "one"
    match value:
        case "one":
            result = 1
        case "two" | "three":
            result = (2, 3)
        case _:
            result = -1
    print(result)

# Run main()
if __name__ == "__main__":
    main()