# Функция для расчета времени накоплений
def calculate_savings(target_price, monthly_income, save_percentage):
    # Считаем, сколько денег откладываем в месяц
    monthly_savings = monthly_income * (save_percentage / 100)
    
    if monthly_savings == 0:
        return "С такими отчислениями накопить не получится! 😢"
    
    # Считаем количество месяцев
    months_needed = target_price / monthly_savings
    return months_needed, monthly_savings

# Главная логика программы
print("--- Калькулятор накоплений на мечту ---")
goal_name = "Ноутбук Gigabyte G6X"
target_sum = 37000  # Цена ноута со скриншота

print(f"Цель: {goal_name} за {target_sum} грн.")

try:
    income = float(input("Сколько ты планируешь зарабатывать в месяц (грн)? "))
    percent = float(input("Какой процент от заработка будешь откладывать (например, 80)? "))
    
    months, save_per_month = calculate_savings(target_sum, income, percent)
    
    print("\n--- РЕЗУЛЬТАТ РАСЧЕТА ---")
    print(f"Ты будешь откладывать по: {save_per_month:.2f} грн в месяц.")
    print(f"Тебе понадобится: {months:.1f} месяцев, чтобы купить ноут!")
    
except ValueError:
    print("Ошибка: вводи только числа!")