# from datetime import datetime, timedelta

                    # #Перетворення рядка у дату
                    # today_date = input("Enter today's date (YYYY.MM.DD): ")

                    # def string_to_date(date_string): 
                    #     return datetime.strptime(date_string, "%Y.%m.%d").date()
                    # Converted_date = string_to_date(today_date)
                    # print(type(Converted_date))

                    # def date_to_string(date):
                    #     return date.strftime("%Y.%m.%d") 
                    # date_string = date_to_string(Converted_date)
                    # print(date_string)
                    # print(type(date_string))


                    # def string_to_date(date_string): 
                    #     return datetime.strptime(date_string, "%Y.%m.%d").date()

                    # def date_to_string(date):
                    #     return date.strftime("%Y.%m.%d") 

                    # date_string = "2024.01.01"
                    # converted_date = string_to_date(date_string)
                    # print(converted_date)
                    # date_string = date_to_string(converted_date)
                    # print(date_string)



# # Преобразование строк birthday в datetime
# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     { "name": "Steve Jobs", "birthday": "1955.3.21"},
#     { "name": "Jinny Lee", "birthday": "1956.3.22"},
#     { "name": "John Doe", "birthday": "1985.01.23"},
#     { "name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# def prepare_user_list(users):
#     # Вариант 1. Сам делал"""
#     # prepared_list = []
#     # for user in users:
#     #     name = user["name"]
#     #     birthday_str = user["birthday"]
#     #     birthday_date = string_to_date(birthday_str)
#     #     prepared_list.append({"name": name, "birthday": birthday_date})
#     # return prepared_list

#     # Вариант 2. Через list comprehension gpt подсказал
#     return [
#         {
#             "name": user["name"], #
#             "birthday": string_to_date(user["birthday"])
#         }
#         for user in users
#     ]
# prepared_users = prepare_user_list(users)   
# print(prepared_users) 


# # Подсчет дней до следующих будних дней 
# def string_to_date(date_string): 
#     return datetime.strptime(date_string, "%Y.%m.%d").date() #

# start_date = string_to_date("2024.03.26") 
# # 
# def find_next_weekday(start_date, weekday): 
#     days_ahead = weekday - start_date.weekday() 
#     if days_ahead <= 0: 
#         days_ahead += 7 
#     return start_date + timedelta(days=days_ahead)
    
# next_monday = find_next_weekday(start_date, 0) # Найти следующий понедельник
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4) # Найти следующую пятницу
# print(next_friday)


# # Определение ближайших дней рождения
# from datetime import datetime, date

# users = [
#     {"name": "Bill Gates", "birthday": "1955.4.23"},
#     { "name": "Steve Jobs", "birthday": "1955.4.25"},
#     ]

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = string_to_date("2024.04.22")
#     print(today)
#     for user in users:
#         user["birthday_this_year"] = user["birthday"].replace(year=today.year)
#         if (user["birthday_this_year"] - today).days <= days and (user["birthday_this_year"] - today).days > 0:
#             upcoming_birthdays.append({
#                    "name": user["name"],
#               "congratulation_date": date_to_string(user["birthday_this_year"])
#            })
              
            
#     return upcoming_birthdays

# upcoming_birthdays = get_upcoming_birthdays(prepare_user_list(users))
# print(upcoming_birthdays)


# # # Подсчет дней до следующих будних дней
# from datetime import datetime, timedelta

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def find_next_weekday(start_date, weekday):
#     print(start_date.weekday())
#     print(weekday)
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5: # Проверяем, является ли день выходным
#         return find_next_weekday(birthday, 0) # Если да, то возвращаем следующий понедельник
#     else:
#         return birthday
    
        
# print(adjust_for_weekend(string_to_date("2025.12.12")))

# # Определение ближайших дней рождения
from datetime import datetime, date, timedelta
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    { "name": "Steve Jobs", "birthday": "1955.12.09"},
 ]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()    

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) # Перевірка, чи не буде припадати день народження вже наступного року
            
          
        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
                      

        congratulation_date_str = date_to_string(birthday_this_year)
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays
print(get_upcoming_birthdays(prepare_user_list(users)))