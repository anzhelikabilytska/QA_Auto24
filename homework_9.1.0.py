def check_word_for_h(word):
    if "h" not in word.lower():
        return "The word does not contain 'h/H'. Please try again!"
    else:
        return "Thank you! You have entered the correct word!"

# Test 1: Word contains lowercase 'h'
assert check_word_for_h("hello") == "Thank you! You have entered the correct word!", "Test 1 Failed"

# Test 2: Word contains uppercase 'H'
assert check_word_for_h("Hello") == "Thank you! You have entered the correct word!", "Test 2 Failed"

# Test 3: Word does not contain 'h' or 'H'
assert check_word_for_h("world") == "The word does not contain 'h/H'. Please try again!", "Test 3 Failed"

# Test 4: Empty string
assert check_word_for_h("") == "The word does not contain 'h/H'. Please try again!", "Test 4 Failed"

# Test 5: Word with only 'h'
assert check_word_for_h("h") == "Thank you! You have entered the correct word!", "Test 5 Failed"

# Test 6: Word with only 'H'
assert check_word_for_h("H") == "Thank you! You have entered the correct word!", "Test 6 Failed"

# Test 7: Word with 'h' in the middle
assert check_word_for_h("ahoy") == "Thank you! You have entered the correct word!", "Test 7 Failed"

# Test 8: Word with 'h' at the end
assert check_word_for_h("match") == "Thank you! You have entered the correct word!", "Test 8 Failed"

# Test 9: Word with multiple 'h's
assert check_word_for_h("hahaha") == "Thank you! You have entered the correct word!", "Test 9 Failed"

# Test 10: Word with 'h' in a case-insensitive manner
assert check_word_for_h("Hat") == "Thank you! You have entered the correct word!", "Test 10 Failed"

print("All tests passed!")
