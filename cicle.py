# fruits = ['apple', 'banana', 'cherry']
# for f in fruits:
#     print(f, end=' ')


# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"{i} є парним числом.")
#     else:
#         print(f"{i} є непарним числом.")

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break
#     break

# number = int(input("number = "))
# if number < 0:
    
# for i in range(5):
#     print(i)
# for i in range(2, 10):
#     print(i)

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)


numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)
for key, value in numbers.items():
    print(key, value)  
for key in numbers.keys():
    print(key)
for value in numbers.values():
    print(value)