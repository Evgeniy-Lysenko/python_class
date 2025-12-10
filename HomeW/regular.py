# Example of using regular expressions in Python with Ukrainian text


# import re

# text = "Вивчення Python може бути веселим. Python - це потужна мова програмування."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.group())
#     print("Позиція початку:", match.start()) # Позиція початку
#     print("Позиція кінця:", match.end())   # Позиція кінця
#     print("Повний збіг:", match.group(0)) # Повний збіг
#     print("Кількість груп:", len(match.groups())) #  Кількість груп
#     print("Всі групи:", match.string) # Повний текст
#     print( match.span()) # Діапазон збігу

# else:
#     print("Не знайдено.")


# import re

# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())
#     print("Позиція початку:", match.start())
#     print("Позиція кінця:", match.end())
# else:
#     print("Не знайдено.")   

# import re

# text = "Моя електронна  адреса: example@example.com Мой nik: use@r123. "
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())
#     print("Позиція початку:", match.start())
#     print("Позиція кінця:", match.end())
# else:
#     print("Електронна адреса не знайдена.")

# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)
#     print("Повний збіг:", match.group(0))
#     print("Позиція початку:", match.start())
#     print("Позиція кінця:", match.end())
#     print("Всі групи:", match.groups())
#     print("Діапазон збігу:", match.span())
#     print("Кількість груп:", len(match.groups()))
#     print("Повний текст:", match.string)
#     print("Ім'я користувача (за індексом):", match.group(1))
#     print("Домен (за індексом):", match.group(2))
#     print("Ім'я користувача (за назвою):", match.group(1))
#     print("Домен (за назвою):", match.group(2))
# else:
#     print("Не знайдено відповідності.")

# import re

# text = "Рік 2023 був складнішим, ніж 2022"
# pattern = r"\d+"
# matches = re.findall(pattern, text)

#datet Developer: Reload Window 
x="datet"

#

# print(matches)

# import re

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку


# import re

# text = "Контакти: example1@example.com, example2@sample.org"
# pattern = r"\w+@\w+\.\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе всі знайдені електронні адреси


# import re

# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name)  

# import re

# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)  

# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)


# import re

# text = "Python - це  проста, але потужна мова програмування."
# pattern = r"\s+"
# words = re.split(pattern, text)

# print(words)  # Виведе список слів у рядку

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку

# import re

# text = "Python - це проста, але потужна мова програмування!"
# pattern = r"[;,\-:!\s]+"
# elements = re.split(pattern, text)

# elements = elements[:-1:]
# print(elements)  # Виведе список частин, розділених пунктуацією

# 
# import re 

# text = "apple#banana!mango@orange;kiwi"
# pattern = r"[#@;!]"
# fruits = re.split(pattern, text) 

# print(fruits) # 
# print 

#all
import datetime
now = datetime.datetime.now() # Поточний час
now.date    

# Функция которая считает факториал 

#   
#date  
