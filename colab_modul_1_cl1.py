# value_one = 5
# value_two = 7
# value_three = -19

# """
# 57 -> 57
# -99 -> 99
# """

# summary = 0
# summary += abs(value_one) # 5
# print(summary)
# summary += abs(value_two) #
# print(summary)
# summary += abs(value_three)
# print(summary)

# sentence_one = "Hello world"
# sentence_two = "Hello " + "world"
# setence_three = "".join(["Hello", " ", "world"]) 
# setence_four = "Hello" + " " + "world"   
# # Відображення змінних
# print(sentence_one, sentence_two, setence_three, setence_four, sep='\n')
# # print(setence_three)
# # print(setence_four)
# print(setence_three[0:5])
# print(sentence_two[0:5])

# # Перевірка рівності і ідентичності
# print(f'Are sentence equal? {sentence_one == sentence_two}')
# print(f'Are sentence identical? {sentence_one is sentence_two}')

# # Перевірка місця збереження у памяті
# print(f'Path of sentence in memory {id(sentence_one)}')
# print(f'Path of sentence in memory {id(sentence_two)}')


# my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

# print(my_list.index(347))
# my_list.insert(my_list.index(347), 100000000)
# print(my_list)

# my_list[my_list.index(7)] = None
# print(my_list)

# my_list[10] = None
# print(my_list)



# my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

# sorted_list = sorted(my_list.copy())
# print(sorted_list)

# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True) #
# print(my_list) # [346, 347, 235, 235, 7, 5, 3, 2, 1, 0, -23, -435]



my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

# print(my_list[::-1]) # [0, -23, -435, 347, 235, 235, 346, 7, 5, 3, 2, 1]
# print(my_list[-1]) # 0
# print(my_list[3:]) # [5, 7, 346, 235, 235, 347, -435, -23, 0]
# print(my_list[:6]) # [1, 2, 3, 5, 7, 346]
# print(my_list[2:10]) # [3, 5, 7, 346, 235, 235, 347, -435]
# print(my_list[:6:-1]) # [0, -23, -435, 347, 235]
# print(my_list[:]) # [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
# print(my_list[2:10:2]) # [3, 7, 235, 347]
# print(my_list[::3]) # [1, 5, 235, -23]
# print(my_list[6:2:-1]) #  [235, 235, 346, 7]

my_list = [[1, 2, 3, 5], [7, 346, 235, 235], 347, -435, -23, 0]

# print(my_list[1][1])
# print(my_list[0][::-1])
# # my_list.insert(3, -100)
# my_list[0].insert(3, -100)
# print(my_list)
# print(my_list[0])

# person = {'name': 'Oleh', "age": 22, "phone": "38(098)*********", 'student': False, 1243: ['test', 'failed']}
# print(person)

# new_data = {'location': 'Ukraine, Lviv', 'lang': "ukr"}
# person.update(new_data)
# print(person)
# print(person.get('name', 'Noname'))
# print(person.get('lang', None))

# person.pop(1243)
# print(person)

# person["age"] = 100
# print(person)

# person['test'] = True
# print(person)

# person.update({(1, ): False})
# print(person)

# Unite several dict into new one
dict_a = {'Alex':12, 'Olga':10}
dict_b = {'Boris':9, 'Kostya':10}
dict_c = {'Ira':11, 'Vova':6}

print(dict_a)
dict_a.update(dict_b)
print(dict_a)
