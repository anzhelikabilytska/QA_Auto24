user_input = input("Type line: ")
unique_symbols = len(set(user_input))
if unique_symbols > 10:
    print(True)
else:
    print(False)