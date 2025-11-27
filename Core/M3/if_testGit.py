# numbers = [10, 4, 201, 21, 12, 2, 132, 7, 1, 18, 3, 12, 6, 15, 4, 27]
# sum_num = 0

# for n in numbers: # iterating through each number in the list
#     if (n % 3) == 0: # checking if the number is divisible by 3
#         sum_num = sum_num + n # adding the number to sum_num if condition is met
#     else:
#         sum_num = sum_num
# print(sum_num) # Output the final sum of numbers divisible by 3

# a = input('Введіть число') #
# a = int(a)

# if a > 1:
#     print('Число додатне') # 
# elif a == 1:
#     print('Число дорівнює 1') # 
# else:
#     print("a <= 0")

# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False
# print(a == c)  # True

# name = None
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")
# else:
#     print("User cannot rent a car") 

# num = abs(int(input("Введите число: ")))

# length = len(str(num))
# print(length)
# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")


# Задаємо конкретне число
# num = int(input())

# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x

# print(f"Result: {result}")

# is_nice = False
# # state = "nice" if is_nice else "not nice" # ternary operator to set state based on is_nice
# # print(f"The state is {state}") #


# some_data = 5
# msg = some_data or "Не було повернено даних" # using 'or' to provide a default message if some_data is None or falsy
# print(msg) # 

# point = ("5, 3")

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# pets = ["fish", "dog", "cat" ]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

