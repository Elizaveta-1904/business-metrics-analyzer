import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    # Данные о выручке по месяцам
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
    }
    df = pd.DataFrame(data)
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    # Пример расчёта KPI (рентабельности)
    revenue = 150000
    cost = 90000
    profitability = calculate_profitability(revenue, cost)
    print(f"Рентабельность: {profitability:.2f}%")


if __name__ == "__main__":
    main()