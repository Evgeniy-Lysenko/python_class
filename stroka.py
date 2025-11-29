# s = "Hello world!"
# # print(s[0])# H
# # print(s[-1])# !
# # print(s[0:5])# Hello
# # print(s[6:])# world!
# # print(s[:5])# Hello
# print(s[::2])# Hlowrd
# # print(s[::-1])# !dlrow olleH

# s = "Hello world!"
# # s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError
# print(s) # Стрічки незмінні (immutable), тому змінити символ за індексом не можна

s = "Hello" 
print(s.upper()) # Виведе 'HELLO'
print(s.lower()) # Виведе 'hello'
print(s.capitalize()) # Виведе 'Hello'
print(s.title()) # Виведе 'Hello'
print(s.replace("H", "J")) # Виведе 'Jello'
print(s.find("e")) # Виведе 1
print(s.find("a")) # Виведе -1, оскільки символ 'a' не знайдено
print(s.split("e")) # Виведе ['H', 'llo']
print(s.split("l")) # Виведе ['He', '', 'o']
print(s.strip("H")) # Виведе 'ello'
print(s.strip("o")) # Виведе 'Hell'

print(my_string) # hello my liTTle friends!
print(my_string.upper()) # HELLO MY LITTLE FRIENDS!
print(my_string.lower()) # hello my little friends!
print(my_string.startswith('hello')) # True
print(my_string.startswith('hi')) # False
print(my_string.endswith('!')) # True
print(my_string.endswith('.')) # False
print(my_string.title()) # Hello My Little Friends!
print(my_string.count('e')) # 3

# s = "Bill Jons"
# print(s.startswith("Bi"))  # Виведе True
# print(s.endswith("ns"))   # Виведе True
# print(s.startswith("Jo"))  # Виведе False
# print(s.endswith("Bi"))    # Виведе False   
# print(s.count("l"))       # Виведе 2, оскільки 'l' зустрічається двічі в рядку
# print(s.count("z"))       # Виведе 0, оскільки 'z' не зустрічається в рядку

# s = "hello world".title()  # Результат: "Hello World"
# print(s)  # Виведе "Hello World"   
# s = "hello world".join(["Start: ", " :End"])  # Результат: "Start: hello world :End"
# print(s)  # Виведе "Start: hello world :End"

# Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))



