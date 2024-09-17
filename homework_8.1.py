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
