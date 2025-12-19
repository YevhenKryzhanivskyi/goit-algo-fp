import random
from collections import Counter
import matplotlib.pyplot as plt


def simulate_two_dice(n_trials: int = 100_000):
    # Симуляція кидання двох шестигранних кубиків
    sums = []
    for _ in range(n_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)

    counts = Counter(sums)

    # Емпіричні ймовірності
    probs_mc = {s: counts[s] / n_trials for s in range(2, 13)}

    # Аналітичні ймовірності
    probs_an = {
        2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36,
        6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36,
        10: 3 / 36, 11: 2 / 36, 12: 1 / 36,
    }

    return counts, probs_mc, probs_an


def plot_probabilities(probs_mc, probs_an):
    # Візуалізація результатів
    sums = list(range(2, 13))
    probs_mc_values = [probs_mc[s] for s in sums]
    probs_an_values = [probs_an[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(
        sums,
        probs_mc_values,
        width=0.4,
        label="Монте-Карло",
        alpha=0.7,
        align="center"
    )
    plt.plot(
        sums,
        probs_an_values,
        "ro-",
        label="Аналітичні",
        linewidth=2
    )

    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.xticks(sums)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()


if __name__ == "__main__":
    n_trials = 100_000
    counts, probs_mc, probs_an = simulate_two_dice(n_trials)

    print("Сума | К-сть | P_MC    | P_аналіт | Різниця")
    for s in range(2, 13):
        p_mc = probs_mc[s]
        p_an = probs_an[s]
        diff = p_mc - p_an
        print(
            f"{s:>3}  | {counts[s]:>5} | "
            f"{p_mc:0.5f} | {p_an:0.5f} | {diff:+0.5f}"
        )

    plot_probabilities(probs_mc, probs_an)
