def sum_of_numbers_in_string(string):
    try:
        numbers = [int(num) for num in string.split(',')]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"

strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
results = [sum_of_numbers_in_string(s) for s in strings]
for result in results:
    print(result)

# Test 1: Basic input with positive integers
assert sum_of_numbers_in_string("1,2,3,4") == 10, "Test 1 Failed"

# Test 2: Input with larger numbers
assert sum_of_numbers_in_string("1,2,3,4,50") == 60, "Test 2 Failed"

# Test 3: Non-numeric input in the string
assert sum_of_numbers_in_string("qwerty1,2,3") == "Не можу це зробити!", "Test 3 Failed"

# Test 4: Empty string
assert sum_of_numbers_in_string("") == 0, "Test 4 Failed"

# Test 5: String with only one number
assert sum_of_numbers_in_string("10") == 10, "Test 5 Failed"

# Test 6: Negative numbers in the string
assert sum_of_numbers_in_string("-1,-2,-3") == -6, "Test 6 Failed"

# Test 7: Mixed positive and negative numbers
assert sum_of_numbers_in_string("-1,2,-3,4") == 2, "Test 7 Failed"

# Test 8: String with spaces around the numbers
assert sum_of_numbers_in_string(" 1 , 2 , 3 , 4 ") == 10, "Test 8 Failed"

# Test 9: String with float values (not supported by the function)
assert sum_of_numbers_in_string("1.5,2.5") == "Не можу це зробити!", "Test 9 Failed"

# Test 10: String with a mix of numbers and text
assert sum_of_numbers_in_string("1,2,abc,4") == "Не можу це зробити!", "Test 10 Failed"

print("All tests passed!")
