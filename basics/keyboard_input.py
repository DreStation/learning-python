def main():
	name = input("What's your name? ")
	print("Nice to meet you", name)

# Tell the interpreter to look for the main() function
# Otherwise, it'll run from top-bottom
# (which is fine in this case, but maybe you don't always want that)
if __name__ == "__main__":
	main()