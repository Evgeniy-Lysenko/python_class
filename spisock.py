# chars = ['a', 'b', 'c'] # створюємо список chars з трьох елементів
# last = chars.pop(1) # видаляємо елемент з індексом 1 і зберігаємо його в змінну last
# print(last)  # Output: b
# print(chars)  # Output: ['a', 'c']
# c_ind = chars.index('c') # знаходимо індекс елемента 'c' в списку chars
# print(c_ind)  # Output: 1

# my_list = [1, 2, 3, 4, 2, 2, 5, 2] # створюємо список my_list з чисел
# count_2 = my_list.count(2) # рахуємо, скільки разів число 2 зустрічається в списку
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

# value = my_list[1]          # берём значение по индексу 2
# count_value = my_list.count(value) # считаем, сколько раз это значение встречается в списке

# print(count_value) # Выведет 4, так как значение 2 встречается 4 раза в списке

# print(len(my_list)) # Выведет 8, так как в списке 8 элементов

# my_list1 = list(reversed(my_list)) # создаём новый список my_list1, который является обратной версией my_list
# print(my_list1) # Выведет [2, 5, 2, 2, 4, 3, 2, 1] 
# print(my_list)  # Выведет [1, 2, 3, 4, 2, 2, 5, 2], исходный список не изменился

# my_list.sort() # сортируем список my_list по возрастанию
# print(my_list) # Выведет [1, 2, 2, 2, 2, 3, 4, 5]

# my_list.reverse() # переворачиваем список my_list
# print(my_list) # Выведет [5, 4, 3, 2, 2, 2, 2, 1]

# words = ["banana", "apple", "cherry"]
# words.sort(key=len) # сортуємо список words за довжиною слів
# print(words)  # Виведе ['apple', 'banana', 'cherry']

# nums = [3, 1, 4, 1, 5, 9, 2]
# sorted_nums = sorted(nums) # створюємо новий відсортований список sorted_nums з елементів nums
# print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
# print(nums)  # Виведе [3, 1, 4, 1, 5, 9, 2], оригінальний список не змінився
# sorted_nums_desc = sorted(nums, reverse=True) # створюємо новий відсортований у зворотньому порядку список sorted_nums_desc
# print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

# words = ["banana", "apple", "cherry"]
# sorted_words = sorted(words, key=len) # створюємо новий відсортований список sorted_words за довжиною слів
# print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']
# print(words)  # Виведе ['banana', 'apple', 'cherry'], оригінальний список не змінився

# chars =  ['a', 'b']
# chars_copy = chars.copy()
# print(chars_copy)  # Виведе ['a', 'b']
# print(chars)  # Виведе ['a', 'b']0	"FLOORS = 5\n"

# print(0/0)

# s1 = "hello" + "world" 

data = [1, 3.11]
some_data = ['python']
data.extend(some_data)
print(data)
data.insert(1, some_data[0])
print(data)
data.reverse()
print(data)