# functions.py
# A script that prints the name of a file with options for full path and margin formatting.
# import sys
# import pathlib

# def print_file_name(file_name, full_name=False, margin=0, margin_items=" "):
#     margin = margin * margin_items
#     if full_name:
#         print(margin + str(file_name.absolute()))
#     else:
#         print(margin = str(file_name.name))

# def main():
#     file_name = pathlib.Path(sys.argv[1])
#     print_file_name(file_name, full_name=True, margin=4, margin_items="*") 
    
# if __name__ == "__main__": 
#     main()

# # Приклад простої функції
# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # Кінець функції say_hello()

# # виклик функції
# say_hello()

# # ще один виклик функції
# say_hello()


# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних як аргументів

    
# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7.1
# print_max(x, y)  # передача змінних як аргументів
# print(type(y))

# def print_max(a: int, b: int):
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise TypeError("Аргументы должны быть целыми числами")

#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')
# x = 5
# y = 7.1
# print_max(x, y)  # передача змінних як аргументів
# print(type(y))


# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15


# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!

# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(5)
# print(check_even)  # Виведе: True

# def modify_string(original: str) -> str: #
#     original = "змінено" #
#     return original #

# str_var = "оригінал" # 
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал

# def modify_list(lst) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1,)

# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)
#     print("Всередині функції:", lst)
#     print("Мой лист в середине", my_list)  # Доступ до зовнішньої змінної
# my_list = [1, 2, 3]
# modify_list(my_list) 
# print(my_list)  # виведе: [1, 2, 3]

# dubble = 0
# def string_to_codes(string: str) -> dict:
#     dubble = 0 #    лічильник дубльованих символів
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#          # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch in codes:
#             dubble += 1
#         else:
#             codes[ch] = ord(ch) 
#     return codes, dubble
# result = string_to_codes(input("Введіть рядок: "))
# print(result)



# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch in codes:
#             continue
#         else: 
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes(input("Введіть рядок: "))
# print(result)

# # Покращена версія функції з поверненням кількості дубльованих символів
# def string_to_codes(string: str) -> tuple[dict, int]:
#     dubble = 0
#     codes = {}

#     for ch in string:
#         if ch in codes:
#             dubble += 1
#         else:
#             codes[ch] = ord(ch)

#     return codes, dubble

# codes, dubble = string_to_codes(input("Введіть рядок: "))

# print("Словник кодів:", codes)
# print("Кількість дубльованих символів:", dubble)

# Глобальна змінна 
# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# # Приклад використання nonlocal
# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"

#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)

#     inner_func() # виклик вкладеної функції

# outer_func() # виклик зовнішньої функції

# Приклад використання nonlocal для зміни змінної зовнішньої функції
# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x
# result = func_outer()  # 5
# print(result) 


# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price*(1 - discount)
        

#     apply_discount() 
#     return price
# result = discount_price(10, 0.5)
# print(result)  # 90.0 

# Приклад використання global
# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)# Значення x складає 2

# # Приклад функції з аргументами за замовчуванням
# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# # використовує значення за замовчуванням для message
# greet("Олексій")  

# # передача власного значення для message
# greet("Марія", message="Добрий день")  


#
# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)

# !!!!!!!
# def get_fullname (first_name, last_name, middle_name=""):
#     return f"{first_name} {middle_name} {last_name}".replace("  ", " ").strip()

# print(get_fullname("Іван", "Іванов", middle_name="Іванович", ))
# print(get_fullname("Петро", "Петров"))

# def format_string(string, length):
#     if len(string) >= length:
#        return string
#     else:
#         gaps = (length - len(string)) // 2
#         return f"{' ' * gaps}{string}"
# print(format_string("привет", 10))

# def first(size, *args):
#     return len((size, *args))
# print(first(5, "first", "second", "third"))

# def second(size, **kwargs):
#     return 1 + len(kwargs) 
# print(second(10, comment_one="Alex", comment_two="Boris"))

# def second(size, **elm_dic):
#     len(second)



# 
# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ', 5)

#  Функція з аргументами за замовчуванням для обчислення реальної вартості товару з урахуванням знижки
# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)

# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, float(input("Введіть знижку на масло у форматі десяткового дробу (наприклад, 0.05 для 5%): ")))
# current_price_sugar = real_cost(price_sugar, 0.07)
# print("Цена на хлеб:", current_price_bread)   # Виведе: 15.0
# print(current_price_butter)  # Виведе: 47.5
# print(current_price_sugar)   # Виведе: 55.8 

# Приклад функції з довільною кількістю позиційних аргументів
# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))
# print(concatenate("Python", " ", "is", " ", "fun", "!"))    

# Приклад функції з довільною кількістю іменованих аргументів
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)
# greet(city="Kyiv", country="Ukraine", profession="Developer")


# # Приклад функції з довільною кількістю позиційних і іменованих аргументів
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, 4, name="Alice", age=25, country="Ukraine")

# # # Приклад розпакування аргументів зі словника
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)


# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120
# print(factorial(0)) # виведе 1


# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

# print(fibonacci(10)) # виведе 55
# print(fibonacci(0))  # виведе 0
# print(fibonacci(1))  # виведе 1
# print(fibonacci(2))  # виведе 1
# print(fibonacci(3))  # виведе 2
# print(fibonacci(4))  # виведе 3
# print(fibonacci(5))  # виведе 5 
# print(fibonacci(6))  # виведе 8
# print(fibonacci(7))  # виведе 13
# print(fibonacci(8))  # виведе 21
# print(fibonacci(9))  # виведе 34
# print(fibonacci(11)) # виведе 89
# print(fibonacci(12)) # виведе 144


# 
# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# 
def factorial(s):
    if s < 2:
        return 1
    else:
        return s * factorial(s - 1)

def number_of_groups(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

print(number_of_groups(50, 7)) 