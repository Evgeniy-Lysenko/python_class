# Работа с случайными числами в Python
# import random

# random.randint(1, 1000) # Генерирует случайное целое число от 1 до 1000
# random.random() # Генерирует случайное число с плавающей точкой от 0.0 до 1.0
# random.uniform(1.5, 10.5) # Генерирует случайное число с плавающей точкой в заданном диапазоне
# random.choice(['apple', 'banana', 'cherry']) # Выбирает случайный элемент из списка
# print(random.sample(range(1, 100), 5)) # Выбирает 5 уникальных случайных чисел из диапазона от 1 до 99
# random.shuffle([1, 2, 3, 4, 5]) # Перемешивает список случайным образом 

# Пример использования random.randrange()
# import random
# print(random.randrange(10))  # Верхня межа є 10, але не включається
# target = random.randrange(1, 11, 2)
# print(f"Ціль: {target}") # Нижня межа 1, верхня межа 11, але не включається, крок 2


# Пример использования random.shuffle() и random.sample()
# import random

# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

# random.shuffle(cards)

# print(f"Перемішана колода: {cards}")
# hand = random.sample(cards, 2)
# print(f"Ваші карти: {hand}")

# Пример использования random.choices()
# import random

# items = ['яблуко', 'банан', 'вишня', 'диня']
# chosen_item = random.choices(items, k=1)
# print(chosen_item)  

# numbers = [1, 2, 3, 4, 5]
# chosen_numbers = random.choices(numbers, k=3)
# print(chosen_numbers)

#  Пример использования random.choices() с весами
# import random

# colors = ['червоний', 'зелений', 'синій']
# weights = [100, 1, 1]
# a = 1
# red = 0
# green = 0
# blue = 0
# while a <= 100:
#     chosen_color = random.choices(colors, weights, k=1)
#     print(chosen_color)  
#     if chosen_color[0] == 'червоний':
#         red += 1
#     elif chosen_color[0] == 'зелений':
#         green += 1
#     else:
#         blue += 1
#     a = a + 1
# print(f"Червоний: {red}, Зелений: {green}, Синій: {blue}")

# Пример выбора случайной команды из списка участников
# import random

# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 4)
# print(f"Команда: {team}")

# Пример генерации случайной цены товара
import random

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.24f}")
