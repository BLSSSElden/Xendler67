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
print(1 "яблоко"
blok = word[1:5]  
oko = word[3:6] 
prinset("Первое слово:", blok)
 print("Второе слово:", oko)
