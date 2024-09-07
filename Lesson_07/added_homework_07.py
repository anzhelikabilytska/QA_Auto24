#Task 1 corrected code
def multiplication_table(number):
    multiplier = 1
    while number * multiplier <= 25:
        print(f"{number}x{multiplier}={number * multiplier}")
        multiplier += 1
multiplication_table(3)
# task 2 Написати функцію, яка обчислює суму двох чисел.
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(5, 7))
# task 3 Написати функцію, яка розрахує середнє арифметичне списку чисел.
def numbers_average():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count
print(numbers_average())
# task 4 Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reverse_sentence(s):
    return s[::-1]
sentence = "Hello, world!"
print(reverse_sentence(sentence))
# task 5 Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def long_word(words):
    if not words:
        return None
    longest = max(words, key=len)
    return longest
words_list = ["The", "last", "exam", "has", "been", "passed"]
print(long_word(words_list))
# task 6 Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))
# task 7
def swap_records(people_records, index_one, index_five):
    people_records[index_one], people_records[index_five] = people_records[index_five], people_records[index_one]
    for record in people_records:
        print(record)
# task 8
def total_sea_area(black_sea, azov_sea):
    return black_sea + azov_sea
black_sea = 436402
azov_sea = 37800
total_area = total_sea_area(black_sea, azov_sea)
print(f"Square of black and azov sea is {total_area}km2")
# task 9
def calculate_computer_cost(monthly_payment, months):
    return monthly_payment * months
monthly_payment = 1179
months = 18
computer_cost = calculate_computer_cost(monthly_payment, months)
print(f"Total computer cost is {computer_cost} uan")
# task 10
def calculate_total_pages(total_images, one_page_contains):
    return (total_images + one_page_contains - 1) // one_page_contains
total_images = 232
one_page_contains = 8
total_pages = calculate_total_pages(total_images, one_page_contains)
print(f"The number of pages required to contain all photos is {int(total_pages)}")