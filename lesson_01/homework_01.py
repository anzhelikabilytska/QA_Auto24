# task 01 == Виправте синтаксичні помилки
# print("Hello", end = " ")
#    print("world!")

print("Hello", end = "!")
print("world!")


# task 02 == Виправте синтаксичні помилки
# hello = "Hello"
# world = "world"
# if True:
# print(f"{hello} {world}!")

hello = "Hello"
world = "world"

if true:
    print(f"{hello} {world}!")


# task 03  == Вcтавте пропущену змінну у ф-цію print
#for letter in "Hello world!":
#   print()

for letter in "Hello world!":
    print(letter)


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
# apples = 2
# banana = x

apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
#1_storona = 1
#?torona_2 = 2
#сторона_3 = 3
#$torona_4 = 4

side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
#perimetery = ? + ? + ? + ?
#print()

perimetery = side_1 + side_2 + side_3 + side_4
print("Sum Sides:", perimetery)


# Задачі 07 -10:
# Переведіть задачі з книги "Математика, 2 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в другому класі

# task 07
#У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
#Скільки всього дерев посадили в саду?

apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = pear_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(f"{total_trees} were planned in the garden")


# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?

morning_degrees = 5
noon_degrees = morning_degrees - 10
evening_degrees = noon_degrees + 4
print(f"{evening_degrees} is in the evening")


# task 09
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?

boys = 24
girls = boys / 2
absence_boys = 1
absence_girls = 2
present_boys = boys - absence_boys
present_girls = girls - absence_girls
total_group = present_boys + present_girls
print(f"Total group is {total_group}")


# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?


book1 = 8
book2 = book1 + 2
book3 = (book1 + book2 ) / 2
total_cost = book1 + book2 + book3
print(f"Books cost is {total_cost}")

