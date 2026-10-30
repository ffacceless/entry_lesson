sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}
def calc(day_sales):
    total = 0
    for name, price, qty in day_sales:   #выручкa за конкретный день
        total += price * qty
    return total
def find_hit(day_sales):
    best_name = ""
    max_qty = 0
    for name, price, qty in day_sales:   #хит продаж за конкретный день
        if qty > max_qty:
            max_qty = qty
            best_name = name
    return best_name
for day in sales:
    day_sales=sales[day]   
    rev=calc(day_sales)
    hit=find_hit(day_sales)
    print(f"{day}: выручка {rev}")
    print(f"Хит {day}: {hit}")
