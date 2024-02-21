import math

print("=== Пункт №1", "="*40)
def form(x, mu, sigma):
    cof = 1 / (sigma * math.sqrt(2 * math.pi))
    exp = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    fr = cof * exp
    return fr
x = 2.5
mu = 0
sigma = 1
result = form(x, mu, sigma)
print("x:", result)
print("=== Пункт №2", "="*40)
john = 3
mary = 5
adam = 6
print("Кількість яблук у Джона, Мері та Адама:", john, mary, adam)
total_apples = john + mary + adam
print("Загальна кількість яблук:", total_apples)
print("=== Пункт №3", "="*40)
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kms_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kms_to_miles, 2), "miles")
print("=== Пункт №4", "="*40)
x = input("Введіть значення x: ")
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3**x - 1
print("y =", y)
print("=== Пункт №5", "="*40)
a = 2  # Кількість годин
seconds = 3600  # Кількість секунд у 1 годині
print("Hours: ", a)  # Виводимо кількість годин
print("Seconds in Hours: ", a * seconds)  # Виводимо кількість секунд у заданій кількості годин
print("Goodbye")
print("=== Пункт №6", "="*40)
a = float(input("Введіть значення a (число): "))
b = float(input("Введіть значення b (число): "))
print("Результат додавання a + b:", a + b)
print("Результат віднімання a - b:", a - b)
print("Результат множення a * b:", a * b)
if b != 0:
    print("Результат ділення a / b:", a / b)
else:
    print("Помилка: ділення на нуль!")
print("\nThat's all, folks!")
print("=== Пункт №7", "="*40)
x = float(input("Введіть значення x: "))
y = 1/(x+(1/(x+(1/(x+(1/x+(1/x)))))))
print("y =", y)
print("=== Пункт №8", "="*40)
hours = int(input("Початковий час (години): "))
minuts = int(input("Початковий час (хвилини): "))
duration = int(input("Тривалість події (хвилини): "))

# Обчислення часу закінчення
ende = (hours + ((minuts + duration) // 60)) % 24
endm = (minuts + duration) % 60

# Виведення результату
print("Подія закінчується о:", str(ende).zfill(2) + ":" + str(endm).zfill(2))
print("="*53)
