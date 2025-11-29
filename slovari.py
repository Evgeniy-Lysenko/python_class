# my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# del my_dict["age"] # Видаляємо пару ключ-значення з ключем "age"
# #print(my_dict) # Виведе {'name': 'Alice', 'city': 'New York'}


# print("age" in my_dict) # Перевіряємо, чи є ключ "age" у словнику, виведе True або False

# key = "age" # Ключ, який ми хочемо перевірити

# if key in my_dict:  # Перевіряємо, чи є ключ у словнику
#     print(f"Ключ '{key}' есть. Значение: {my_dict[key]}") # Виведе значення, якщо ключ існує
# else:
#     print(f"Ключа '{key}' нет в словаре.") # Виведе повідомлення, якщо ключ не існує

# print(my_dict.get("name")) # Використовуємо метод get для отримання значення за ключем "name"
# print(my_dict.get("age")) # Використовуємо метод get з значенням за замовчуванням для ключа "age"
# print(my_dict["name"]) # Використовуємо прямий доступ для отримання значення за ключем "name"


data = {} # створюємо порожній словник data
age = 22
name = {"name": "Evgen"}
hobbies = {"hobbies": ["sec", "data"]}
info = {"status": "student", "school": "GoIT"}
data.update(name) # додаємо пару ключ-значення з ключем "name" до словника data
key = "age" # створюємо змінну key зі значенням "age"
data[key] = age # додаємо пару ключ-значення з ключем "age" до словника data
data.update(hobbies)
data.update(info)
print(data)
