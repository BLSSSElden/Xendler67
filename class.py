year = 0
def is_leap_years(year):
    for i in range(2000,2025):
        if i%4==0:
            year+=1

def digit_sum(n):
    return sum(int(digit) for digit in str(n))
def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number).zfill(6)
    first_half = ticket_str[:3]
    second_half = ticket_str[3:]
    return digit_sum(first_half) == digit_sum(second_half)
number = 123321
if is_lucky_ticket(number):
    print(f"Билет {number} — СЧАСТЛИВЫЙ!")
else:
    print(f"Билет {number} — обычный.")

def find_index(lst, value):
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1

matrix = []
print("Введите матрицу 3x3 (по 3 числа через пробел в каждой строке):")
for i in range(3):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    matrix.append(row)
total_sum = 0
for row in matrix:
    total_sum += sum(row)
diagonal_sum = 0
for i in range(3):
    diagonal_sum += matrix[i][i]
print("\nВведенная матрица:")
for row in matrix:
    print(row)
print(f"\nСумма всех элементов: {total_sum}")
print(f"Сумма элементов главной диагонали: {diagonal_sum}")

matrix = [
    [7, 8, 9]
    [1, 2, 3]
]
max_val = max(max(row) for row in matrix)
row, col = next((r, c) for r, row in enumerate(matrix) for c, val in enumerate(row) if val == max_val)
print(f"Максимум: {max_val} (Строка: {row + 1}, Столбец: {col + 1})")

matrix = [
    [4, 5, 6]   
    [3, 2, 1]
]
max_row = max(matrix, key=sum)
print(f"Строка с максимальной суммой: {max_row}")
print(f"Её сумма: {sum(max_row)}")

matrix = [
    [4, 5, 6]   
    [3, 2, 1]
]
shifted_matrix = [row[1:] + row[:1] for row in matrix]
print("Матрица после сдвига:")
for row in shifted_matrix:
    print(row)

word = "Информатика"
result = word[1] + word[3]
print(result) 
word = "Программа"
half_length = len(word) // 2
first_half = word[:half_length]
print(first_half)
word = "яблоко"
blok = word[1:5]  
oko = word[3:6] 
print("Первое слово:", blok)
print("Второе слово:", oko)

balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print(f"Внесено {amount}. Баланс: {balance}")
def withdraw(amount):
    global balance
    if amount > balance:
        print("Недостаточно средств!")
    else:
        balance -= amount
        print(f"Снято {amount}. Баланс: {balance}")
def check_balance():
    print(f"Текущий баланс: {balance}")

from itertools import groupby
s = "aaabbc"
res = "".join(f"{k}{len(list(g))}" for k, g in groupby(s))
print(res) 
matrix = [
    [1, 2, 3, 4]
    [8, 10, 12, 14]
]

for i, row in enumerate(matrix, 1):
    count = sum(1 for x in row if x % 2 == 0)
    print(f"Строка {i}: {count} чётных чисел")

matrix = [
    [1, 2, 3, 4]
    [8, 10, 12, 14]
]
row_num = 1
for row in matrix:
    count = sum(1 for x in row if x % 2 == 0)
    print(f"Строка {row_num}: {count} чётных чисел")
    row_num += 1

matrix = [
    [4, -5, 6]
    [-1, 0, 2]
]

print("Строки без отрицательных чисел:")
for row in matrix:
    if all(x >= 0 for x in row):
        print(row)

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
print("Введите элементы матрицы (через пробел для каждой строки):")
for i in range(rows):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    matrix.append(row)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > 0:
            matrix[i][j] = 1 
        elif matrix[i][j] < 0:
            matrix[i][j] = -1 
print("\nМатрица после замены:")
for row in matrix:
    print(row)

with open("numbers.txt", "r") as file_in:
    content = file_in.read() 
numbers = list(map(int, content.split()))
positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
with open("positive.txt", "w") as file_out:
    output_text = " ".join(map(str, positive_numbers))
    file_out.write(output_text)
print("Файл positive.txt успешно создан и заполнен!")

import string_helpers as sh
word1 = "шалаш"
word2 = "программа"
phrase = "А роза упала на лапу Азгора"
print(f"'{word1}' — палиндром?", sh.is_palindrome(word1))     
print(f"'{word2}' — палиндром?", sh.is_palindrome(word2))    
print(f"'{phrase}' — палиндром?", sh.is_palindrome(phrase))

def is_palindrome(s):
    clean_s = "".join(s.split()).lower()
    return clean_s == clean_s[::-1]



import math
def circle_area(radius):
    return math.pi * (radius ** 2)
def rectangle_area(width, height):
    return width * height

def km_to_miles(km):
    return km * 0.621371
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32





f
import shapes
import converter
f= 5
w, h = 4, 6
print(f"Площадь круга с радиусом {r}: {shapes.circle_area(r):.2f}")
print(f"Площадь прямоугольника {w}x{h}: {shapes.rectangle_area(w, h)}")
print("-" * 30)
distance_km = 10
temp_c = 25
print(f"{distance_km} км — это {converter.km_to_miles(distance_km):.2f} миль")
print(f"{temp_c}°C — это {converter.celsius_to_fahrenheit(temp_c):.1f}°F")

text = "python java python csharp java python."
words = text.replace(".", "").split()
most_common_word = max(set(words), key=words.count)
print(f"Самое часто встречающееся слово: {most_common_word}")
print(f"Оно встречается {words.count(most_common_word)} раза.")

with open("words.txt", "r") as file:
    text = file.read()
words = text.replace(".", "").split()
most_common = max(set(words), key=words.count)
print("Самое частое слово:", most_common)

def find_unique_elements(matrix):
    counts = {} 
    for row in matrix:
        for element in row:
            counts[element] = counts.get(element, 0) + 1
    unique_elements = [item for item, count in counts.items() if count == 1]
    return unique_elements
matrix = [
    [3, 1, 8]
    [6, 1, 7]
]
print("Уникальные элементы:", find_unique_elements(matrix))


import math
def area(radius):
    return math.pi * (radius ** 2)
def perimeter(radius):
    return 2 * math.pi * radius

def area(width, height):
    return width * height
def perimeter(width, height):
    return 2 * (width + height)

while True:
    try:
        age = int(input("Пожалуйста, введите ваш возраст (число): "))
        break
    except ValueError:
        print("Ошибка! Вы ввели не число. Попробуйте ещё раз.")
print(f"Спасибо! Ваш возраст: {age}")


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
pint(safe_divide(10, 2)) 
prnt(safe_divide(5, 0))  
prnt("Hello")

