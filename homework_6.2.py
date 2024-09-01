#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
#Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
while True:
    user_input = input("Enter the word: ")
    if "h" not in user_input.lower():
        print("The word does not contain 'h/H'. Please try again!")
    else:
        print("Thank you! You have entered the correct word!")
        break


