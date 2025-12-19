items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Алгоритм жадібного вибору:
    # - сортує страви за співвідношенням калорій до вартості
    # - вибирає страви, поки не вичерпає бюджет
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    chosen = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return {
        "chosen": chosen,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


def dynamic_programming(items, budget):
    # Алгоритм динамічного програмування:
    # - створює таблицю для збереження максимальних калорій для кожної вартості
    # - заповнює таблицю, розглядаючи кожен елемент
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n_items = len(names)

    dp = [[0] * (budget + 1) for _ in range(n_items + 1)]

    for i in range(1, n_items + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    chosen = []
    w = budget
    for i in range(n_items, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n_items][budget]
    total_cost = sum(items[name]["cost"] for name in chosen)

    return {
        "chosen": chosen[::-1],
        "total_cost": total_cost,
        "total_calories": total_calories
    }


if __name__ == "__main__":
    budget = 100
    print("Greedy:", greedy_algorithm(items, budget))
    print("Dynamic Programming:", dynamic_programming(items, budget))