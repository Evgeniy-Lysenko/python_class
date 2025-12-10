# Код для демонстрації math  Python
# import math

# # Вихідне число
# x = 3.7

# # Використання різних методів округлення
# ceil_result = math.ceil(x)  # Округлення вгору
# floor_result = math.floor(x)  # Округлення вниз
# trunc_result = math.trunc(x)  # Відсікання дробової частини

# print(ceil_result, floor_result, trunc_result)

# # Використання round для округлення до найближчого цілого
# import decimal
# x = decimal.Decimal("2.3")
# print(x.quantize(decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


# Приклад використання модуля math
# import math

# # Використання констант
# print(f"{math.pi:.0f}")  # Значення числа π з точністю до 4 знаків після коми
# print(f"{math.e:.1f}")   # Значення числа e з точністю до 4 знаків після коми
# print(f"{math.tau:.4f}")  # Значення числа τ з точністю до 4 знаків після коми


# # Тригонометрія
# angle = math.radians(60)  # Конвертація з градусів у радіани
# print(math.sin(angle))  # Синус кута

# # Корінь числа
# print(math.sqrt(9))  # Квадратний корінь з 9

# # Логарифми
# print(math.log(10, 2))  # Логарифм 10 за основою 2

#  Перевірка точності чисел з плаваючою комою
import math
print(0.1 + 0.2 == 0.3)  # Це повертає False
print(math.isclose(0.1 + 0.2, 0.3))  # Це повертає True

print(math.log(1000, 10))  # Логарифм 1000 за основою 10
print(math.log2(1024))     # Логарифм 1024 за основою 2
print(math.log10(100))     # 