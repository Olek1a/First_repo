import random

def get_numbers_ticket(min, max, quantity):
    # 1. Перевірка правильності введених даних (валідність)
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    # 2. Створюємо діапазон чисел від min до max
    # range не включає останнє число, тому додаємо +1
    numbers_range = range(min, max + 1)

    # 3. Вибираємо унікальні випадкові числа
    # random.sample одразу гарантує унікальність
    picked_numbers = random.sample(numbers_range, quantity)

    # 4. Повертаємо відсортований список
    return sorted(picked_numbers)

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")
