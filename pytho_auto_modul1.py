# my_list = []
# my_list.insert(0, 2024)
# my_list.insert(1, "Python")
# my_list.insert(2, 3.12)
# print(my_list)

# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# print(my_list)
# my_list.insert(1, some_data[0])
# print(my_list)
# my_list.reverse()
# print(my_list)

# data = {"year": 2024, "language": "Python", "version": 3.12}
# print(data)

cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update({"nick": "Simon", "age": 7, "characteristics": ["ласковый", "кусается"]})
print(cat)
age = cat.get("age")
print(age)
cat.update(info)
print(cat)