#task1
alice_in_wonderland = """/
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, 
"if you only walk long enough."
"""
#task2
single_quote_count = alice_in_wonderland.count("'")
print(f"Found {single_quote_count} single quote(s).")
#task3
print(alice_in_wonderland)
#task4
#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-ське моря разом?
black_sea = 436402
azov_sea = 37800
s = black_sea+azov_sea
print(f"Square of black and azov sea is {s}km2")
#task4
#Мережа супермаркетів має 3 склади, де всього розміщено
#375 291 товар. На першому та другому складах перебуває
#250 449 товарів. На другому та третьому – 222 950 товарів.
#Знайдіть кількість товарів, що розміщені на кожному складі.
total_stored_goods = 375291
sum_of_first_and_second_storages = 250449
sum_of_second_and_third_storages = 222950
third_storage = total_stored_goods - sum_of_first_and_second_storages
first_storage = total_stored_goods - sum_of_second_and_third_storages
second_storage = sum_of_first_and_second_storages - first_storage
print(f"First storage has stored {first_storage} goods")
print(f"Second storage has stored {second_storage} goods")
print(f"Third storage has stored {third_storage} goods")
# task 06
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.
monthly_payment = 1179
computer_cost = 1179 * 6
print(f"Total computer cost is {computer_cost} uan")
#task 07
#Знайди остачу від діленя чисел:
#a) 8019 : 8     d) 7248 : 6
#b) 9907 : 9     e) 7128 : 5
#c) 2789 : 5     f) 19224 : 9
a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224
rest_a = a / 8
rest_b = b / 9
rest_c = c / 5
rest_d = d / 6
rest_e = e / 5
rest_f = f / 9
print(f"Remaining amount {a} на 8: {rest_a}")
print(f"Remaining amount {b} на 9: {rest_b}")
print(f"Remaining amount {c} на 5: {rest_c}")
print(f"Remaining amount {d} на 6: {rest_d}")
print(f"Remaining amount {e} на 5: {rest_e}")
print(f"Remaining amount {f} на 9: {rest_f}")
#task 08
#Іринка, готуючись до свого дня народження, склала список того,
#що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
#для даного її замовлення.
#Назва товару    Кількість   Ціна
#Піца велика     4           274 грн
#Піца середня    2           218 грн
#Сік             4           35 грн
#Торт            1           350 грн
#Вода            3           21 грн
large_pizza_quantity = 4
large_pizza_price = 274
medium_pizza_quantity = 2
medium_pizza_price = 218
juice_quantity = 4
juice_price = 35
cake_quantity = 1
cake_price = 350
water_quantity = 3
water_price = 21
total_large_pizza_cost = large_pizza_quantity * large_pizza_price
total_medium_pizza_cost = medium_pizza_quantity * medium_pizza_price
total_juice_cost = juice_quantity * juice_price
total_cake_cost = cake_quantity * cake_price
total_water_cost = water_quantity * water_price
total_cost = (total_large_pizza_cost + total_medium_pizza_cost + total_juice_cost + total_cake_cost + total_water_cost)
print(f"Total order price is {total_cost} uan")
#task 09
#Ігор займається фотографією. Він вирішив зібрати всі свої 232
#фотографії та вклеїти в альбом. На одній сторінці може бути
#розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
#Ігорю, щоб вклеїти всі фото?
total_images = 232
one_page_contains = 8
total_pages = total_images / one_page_contains
print(f"The number of pages required to contain all photos is {int(total_pages)}")
#task 10
#Родина зібралася в автомобільну подорож із Харкова в Буда-
#пешт. Відстань між цими містами становить 1600 км. Відомо,
#що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
#становить 48 літрів.
#1) Скільки літрів бензину знадобиться для такої подорожі? 144
#2) Скільки щонайменше разів родині необхідно заїхати на зап-
#равку під час цієї подорожі, кожного разу заправляючи пов-
#ний бак? 144/8 = 3
distance = 1600
fuel_tank = 48
fuel_per_100km = 9
total_fuel_required = distance * fuel_per_100km / 100
print(f"Total fuel required for this trip is {total_fuel_required}l")
stops_required = total_fuel_required / fuel_tank
print(f"Stops required: {int(stops_required)} times")
