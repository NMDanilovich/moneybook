
def free_money(income: list[float], expenses: list[float]):
    free = sum(income) - sum(expenses)
    
    return free

income = [6250., 20476.05]

expenses = [15000./2, 700., 8000., 4570./2, 1000., 770., 125., 2432.3, 70.]

free = free_money(income=income, expenses=expenses)
print(free)
