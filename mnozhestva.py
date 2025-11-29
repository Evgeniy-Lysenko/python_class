# a = set('hello')
# print(a)  # Виведе {'e', 'h', 'l', 'o'}
# b = {1, 2, 3, 4, 5}
# print(b)  # Виведе {1, 2, 3, 4, 5}
# c = set([1, 2, 2, 3, 4, 4, 5])
# print(c)  # Виведе {1, 2, 3, 4, 5}
# d = set((1, 2, 3, 4, 5))
# print(d)  # Виведе {1, 2, 3, 4, 5}
# e = set({1: 'a', 2: 'b', 3: 'c'})
# print(e)  # Виведе {1, 2, 3}    


# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)  # {1, 2, 3, 4}
# numbers.remove(3)
# print(numbers)  #  {1, 2, 4}
# numbers.discard(3)  # не викликає помилку, якщо елемент відсутній

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

# my_frozenset = frozenset([1, 2, 3, 4, 5])
# print(my_frozenset)  # Виведе frozenset({1, 2, 3, 4, 5})
# # my_frozenset.add(6)  # Викличе помилку, оскільки frozenset незмінний

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(a|b)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})


# my_set = set('hi there!')
# print(my_set)
# print(set(sorted(my_set)))
# print(sorted(my_set))
