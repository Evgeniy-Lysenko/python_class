# the number of days between a given date and a current date
from datetime import datetime

def get_days_from_today(input_date): # Розрахунок кількості днів між двома датами
    try:
            input_date = datetime.strptime(input_date, "%Y-%m-%d") # Перетворення дати в об'єкт datetime 
            today_date = datetime.now() # Отримання поточнї дату
            return (input_date - today_date).days 
    except ValueError:
            return "Invalid date format. Please try again." # Повідомлення про помилку при неправильному форматі дати

input_date = input("Enter a date in the format YYYY-MM-DD: ") # Введення дати в форматі YYYY-MM-DD

print(get_days_from_today(input_date))  # Виклик функції для отримання кількості днів між двома датами

