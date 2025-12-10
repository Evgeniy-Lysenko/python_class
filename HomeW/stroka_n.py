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

# s = "Hello" 
# print(s.upper()) # Виведе 'HELLO'
# print(s.lower()) # Виведе 'hello'
# print(s.capitalize()) # Виведе 'Hello'
# print(s.title()) # Виведе 'Hello'
# print(s.replace("H", "J")) # Виведе 'Jello'
# print(s.find("e")) # Виведе 1
# print(s.find("a")) # Виведе -1, оскільки символ 'a' не знайдено
# print(s.split("e")) # Виведе ['H', 'llo']
# print(s.split("l")) # Виведе ['He', '', 'o']
# print(s.strip("H")) # Виведе 'ello'
# print(s.strip("o")) # Виведе 'Hell'

# print(my_string) # hello my liTTle friends!
# print(my_string.upper()) # HELLO MY LITTLE FRIENDS!
# print(my_string.lower()) # hello my little friends!
# print(my_string.startswith('hello')) # True
# print(my_string.startswith('hi')) # False
# print(my_string.endswith('!')) # True
# print(my_string.endswith('.')) # False
# print(my_string.title()) # Hello My Little Friends!
# print(my_string.count('e')) # 3

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


# print("Hello  my little\rsister")
# print('It\'s a beautiful day')
# print("He said, \"Hello\"")

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("!", start, end)) # 5
# print(s.find("!")) # -1


# s = 'Some words'

# print(s.find("o"))
# print(s.rfind('o'))


# s = 'Some words'

# print(s.index("a"))
# print(s.rindex('o'))


# text = "hello world"
# print(type(text))  # Виведе: <class 'str'>
# result = text.split()
# print(type(result))  # Виведе: <class 'list'>
# print(result)  # Виведе: ['hello', 'world']

# text = "apple_banana,cherry"
# result = text.split('_')
# print(result)  # Виведе:  ['apple', 'banana,cherry']


# list_of_strings = ['Hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'
# result_with_comma = ', '.join(list_of_strings)
# print(result_with_comma)  # Виведе: 'Hello, world'  

# elements = ['earth', 'air', 'fire', 'water']
# result = ', \r'.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'
# path = ['home', 'user', 'documents', 'file.txt']
# file_path = '/'.join(path)
# print(file_path)  # Виведе: 'home/user/documents/file.txt'

# text = "Hello world core!"
# new_text = text.replace("world", "Python")
# print(type(new_text))  # Виведе: <class 'str'>
# print(new_text)  


# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 1)
# print(new_text)  


# print('TestHook Test'.removeprefix('Test').removesuffix('Test')) # Hook
# print('TestHook'.removeprefix('Hook')) # TestHook
# print('TestHook'.removesuffix('Hook')) # Test
# print('TestHook'.removesuffix('Test')) # TestHook

# Розділення рядка на три частини
# text = "apple_banana_cherry"
# _, _, result = text.split('_')
# print(result)  # Виведе:  ['apple', 'banana,cherry']

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?') # Виведе все, що після знаку питання
# print(query)
# obj_query = {} # Створюємо порожній словник
# for el in query.split('&'): # Розділяємо рядок за символом &
#     print(el)
#     key, value = el.split('=') # Розділяємо кожен елемент за символом =
#     print(key, value)
#     obj_query.update({key: value.replace('+', ' ')}) # Додаємо пару ключ-значення до словника, замінюючи + на пробіл у значенні
# print(obj_query)


# number = "12345"
# print(number.isdigit())  # Виведе: True

# text = "Number123"
# print(text.isdigit())  # Виведе: False
# alpha = "HelloWorld"
# print(alpha.isalpha())  # Виведе: True
# alphanumeric = "Hello123"
# print(alphanumeric.isalnum())  # Виведе: True
# special_chars = "Hello@123"
# print(special_chars.isalnum())  # Виведе: False
# whitespace = "   "
# print(whitespace.isspace())  # Виведе: True
# mixed = " Hello "
# print(mixed.isspace())  # Виведе: False


# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")


# intab = "aeiou"
# outtab = "@2105"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))


# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     print(MAP)
#     MAP[ord(s.lower())] = c
#     print(MAP)
# print(MAP)
# result = "34 DF 56 aC".translate(MAP)
# print(result)

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v
#     print(table_morze_dict)
# string = "SOS"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)

morze_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

string = "sos"
result = ""

for ch in string.upper():
    if ch in morze_dict:
        result += morze_dict[ch] + " "  # добавляем пробел между кодами
    else:
        result += " "  # для пробелов или других символов

print(result)
