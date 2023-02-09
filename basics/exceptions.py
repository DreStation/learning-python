try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError as e:
    print("That's not a number!")
    print(e)
finally:
    print("This always runs")