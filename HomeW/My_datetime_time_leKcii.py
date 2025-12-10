
# # Using the datetime module to get current date and time
# import datetime
# now = datetime.datetime.now()
# print(now)

#  Alternative approach
# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute) # 
# print(current_datetime.second) # 
# print(current_datetime.microsecond) #
# print(current_datetime.tzinfo) # prints None if no timezone is set
# print(current_datetime) # prints the full datetime object


from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())
print(current_datetime.strftime("%Y-%m-%d %H:%M:%S")) # Formatted date and time
print(current_datetime.isoformat()) # ISO 8601 format
print(current_datetime.weekday()) # Day of the week as an integer (0=Monday, 6=Sunday)
print(current_datetime.ctime()) # Human-readable string representation  of the date and time
print(current_datetime.timestamp()) # Unix timestamp
print(current_datetime.utcoffset()) # UTC offset, None if no timezone is set
print(current_datetime.replace(year=2025)) # Replace year with 2025    


# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime   
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
# print(type(time_part))



# from datetime import datetime, timedelta
# # Поточний час
# now = datetime.now()
# print("Поточний час:", now) 
# hour = now.hour
# minute = now.minute
# second = now.second
# print(f"Години: {hour}, Хвилини: {minute}, Секунди: {second}")

# day_now = datetime.date(now)
# print("Поточна дата:", day_now)
# print(f"Рік: {day_now.year}, Місяць: {day_now.month}, День: {day_now.day}")
# print("День тижня (0-Понеділок, 6-Неділя):", (day_now.weekday() +1))
# print("День року:", day_now.timetuple().tm_yday)
# print("Чи є високосним рік?:", day_now.year % 4 == 0 and (day_now.year % 100 != 0 or day_now.year % 400 == 0))
# print("Кількість днів у місяці:", (datetime(now.year, now.month % 12 + 1, 1) - timedelta(days=1)).day)
# print("Часова зона:", now.tzinfo)
# print
# # Дата і час через 5 днів
# future_date = now + timedelta(days=5)
# print("Дата і час через 5 днів:", future_date)  
# # Дата і час 3 дні тому
# past_date = now - timedelta(days=3)
# print("Дата і час 3 дні тому:", past_date)  
# # Різниця між двома датами
# date1 = datetime(2023, 12, 20)
# date2 = datetime(2023, 12, 14)
# difference = date1 - date2


# import datetime

# day_now = datetime.datetime.now()
# days = ["Понеділок","Вівторок","Середа","Четвер","П’ятниця","Субота","Неділя"]

# day_number = day_now.weekday() + 1   # 1–Понеділок, 7–Неділя
# day_name = days[day_now.weekday()]

# print(f"Сьогодні {day_number}-й день тижня: {day_name}")
# # print(f"Сьогодні {day_now.isoweekday()}-й день тижня: {days[day_now.isoweekday()-1]}")

# days[5] = "Ехху Субота!"
# print(days)

# day_name = days[day_now.weekday()]
# print(f"Сьогодні {day_number}-й день тижня: {day_name}")

# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"

# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
# print(date_part)
# print(time_part)
# date_part2 = datetime.datetime(2023, 12, 14, 12, 30, 15)
# print(date_part2)

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 7, 12, 3, 3)
# datetime2 = datetime(2023, 3, 15, 3, 5, 8)
# print(datetime1, datetime2)


# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# # Різниця між двома датами
# difference = datetime2 - datetime1
# print(difference)  #    Виведе "8 days, 0:02:05"   
# print(difference.days)  #  Виведе 8
# print(difference.seconds)  # Виведе 125 (кількість секунд понад повні дні)    
# print(difference.total_seconds())  #  Виведе 691205.0 (загальна кількість секунд у різниці)  
# print((difference.total_seconds()/60)/60)  #   Виведе 191.44583333333333 (загальна кількість годин у різниці)


# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)
# print("Дні:", delta.days)
# print("Секунди:", delta.seconds)
# print("Мікросекунди:", delta.microseconds)
# print("Загальна кількість секунд:", delta.total_seconds())  

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0
# print(difference.days)  # 365   

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)
# future_date = now - timedelta(days=10)  # Віднімаємо 10 днів від поточної дати
# print(future_date)  

# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2025, month=12, day=1)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")
# # Відновлення дати з порядкового номера
# restored_date = datetime.fromordinal(ordinal_number)
# print(f"Відновлена дата з порядкового номера {ordinal_number} становить {restored_date}")

# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)
# # Альтернативний спосіб розрахунку кількості днів
# difference = current_date - napoleon_burns_moscow
# print(difference.days)  #

# from datetime import datetime

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу
# # Конвертація timestamp назад в datetime
# converted_datetime = datetime.fromtimestamp(timestamp)
# print(converted_datetime)  # Виведе datetime, відповідний до timestamp  


# from datetime import datetime

# now = datetime.now()
# print(now)

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)
# # Форматування лише часу
# formatted_time_only = now.strftime("%H:%M:%S")
# print(formatted_time_only)  


# from datetime import datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
# # Виведення окремих компонентів дати
# print("Рік:", datetime_object.year)
# print("Місяць:", datetime_object.month)
# print("День:", datetime_object.day) 

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)
# # Конвертація назад з формату ISO 8601 в об'єкт datetime
# converted_datetime = datetime.fromisoformat(iso_format)
# print(converted_datetime)  # Виведе об'єкт datetime, відповідний до ISO 8601 формату    


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()

# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня
# # Порівняння з weekday()
# day_of_week_weekday = now.weekday() + 1  # Додаємо 1, щоб відповідати формату isoweekday()
# print(f"Сьогодні (за weekday() + 1): {day_of_week_weekday}")    


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
# # Виведе ISO рік, номер тижня та день тижня (1-Понеділок, 7-Неділя)     


# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC
# print("Локальний час:", local_now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# print("UTC час:", utc_now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))   


# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  
# # Виведе поточний час в Східному часовому поясі (UTC-5)
# print("Час у Східному часовому поясі:", eastern_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

# from datetime import datetime, timezone, timedelta

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC
# # Виведе локальний час з інформацією про часову зону
# print("Локальний час:", local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# # Виведе час в UTC з інформацією про часову зону
# print("Час в UTC:", utc_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))    

# from datetime import datetime, timezone, timedelta

# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
# print(timezone_datetime)  # Виведе дату і час з інформацією про часову зону

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)
# # Конвертація назад з формату ISO 8601 в об'єкт datetime з урахуванням часової зони
# converted_datetime_with_timezone = datetime.fromisoformat(iso_format_with_timezone)
# print(converted_datetime_with_timezone)  # Виведе об'єкт datetime з інформацією про часову зону 

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")
# local_time = time.localtime(current_time)
# print(local_time)
# print("Локальний час:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))
# utc_time = time.gmtime(current_time)
# print("UTC час:", time.strftime("%Y-%m-%d %H:%M:%S", utc_time))     


# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")
# # Затримка на 5 секунд  

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")
# # Конвертація поточного часу в читабельний формат   

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")


# import time

# # Записуємо час на початку виконання
# start_time = time.perf_counter()
# print(start_time)

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()
# print(end_time)

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")
# # Використання time.perf_counter() для вимірювання часу виконання коду


import time
start_time = time.perf_counter()
print(start_time)
print("Початок паузи")
time.sleep(5)
print("Кінець паузи")
end_time = time.perf_counter()
print(end_time)
print(f"Час паузи: {end_time - start_time} секунд") 
# Затримка на 5 секунд  