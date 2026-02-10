from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо дату  в рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
        target_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - target_date
        return difference.days
    
    except ValueError:
        # Якщо формат дати неправильний (виникла помилка ValueError)
        return "Неправильний формат дати! Використовуйте РРРР-ММ-ДД."

# Тепер перевіряємо:
print(get_days_from_today("2026-10-09"))  # Працює як раніше
print(get_days_from_today("13.14.2000"))  # Не впаде, а напише попередження