FLOORS = 10 # Кількість поверхів в під'їзді
APARTMENTS_PER_FLOOR = 4 # Кількість квартир на поверсі

apartment_number = int(input('Enter apartment number: ')) # Номер квартири
apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR # Загальна кількість квартир в під'їзді
entrance_number = (apartment_number - 1) // apartments_per_entrance + 1 # Номер під'їзду
floor_number = ((apartment_number - 1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1 # Номер поверху
print(f"Entrance number {entrance_number}, Floor number {floor_number}") # Виведення результату