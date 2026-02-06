from datetime import datetime

def get_days_from_today(date):
    # 1. Перетворюємо рядок у об'єкт datetime
    # Формат %Y-%m-%d — це якраз РРРР-ММ-ДД
    target_date = datetime.strptime(date, "%Y-%m-%d")
    
    # 2. Отримуємо поточну дату
    today = datetime.today()
    
    # 3. Рахуємо різницю
    difference = today - target_date
    
    # 4. Повертаємо кількість днів як ціле число (.days)
    return difference.days

# Перевірка:
print(get_days_from_today("2020-10-09")) # Виведе кількість днів, що минули
print(get_days_from_today("2026-10-09")) # Виведе від'ємне число, бо дата в майбутньому