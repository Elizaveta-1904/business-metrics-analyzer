print("Hello, Git!")
print("Анализ бизнес-метрик")


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


revenue = 100000
cost = 70000

profitability = calculate_profitability(revenue, cost)

print(f"Рентабельность: {profitability:.2f}%")