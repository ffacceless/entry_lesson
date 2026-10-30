sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}
word="выручка"
def calc(day_sales):
    total = 0
    for name, price, qty in day_sales:
        total += price * qty
    return total
def find_hit(day_sales):
    best_name = ""
    max_qty = 0
    for name, price, qty in day_sales:
        if qty > max_qty:
            max_qty = qty
            best_name = name
    return best_name
def get_best_day(sales):
    best_day=""
    max_rev=0
    for day in sales:
        rev=calc(sales[day]) 
        if rev>max_rev:
            max_rev=rev
            best_day=day
    return best_day,max_rev
def get_average(sales):
    total_week=0
    days_count=0          #средняя выручка с округлением до рубля
    for day in sales:
        total_week+=calc(sales[day])
        days_count+=1
    avg=round(total_week/days_count)
    return avg
total_week_rev=0    #вывод всего счета
for day in sales:
    day_sales=sales[day]    
    rev=calc(day_sales)
    hit=find_hit(day_sales)
    total_week_rev+=rev    
    print(f"{day}: {word} {rev}")
    print(f"Хит {day}: {hit}")
best_day,best_day_rev=get_best_day(sales)
avg_rev=get_average(sales)
print(f"итоговая {word} за неделю: {total_week_rev}")
print(f"день с максимальной {word}ой: {best_day} ({best_day_rev})")
print(f"средняя {word} за день: {avg_rev} руб.")
