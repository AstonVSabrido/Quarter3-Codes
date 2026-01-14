import numpy as np

names = ["Jane", "Marvoun", "Aston"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 6100, 4800, 5000, 5300],  # Jane
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6700]   # Aston
])

daily_totals = np.sum(steps, axis=0)

for i in range(len(days)):
    print(f"{days[i]} | Total Steps: {daily_totals[i]}")

most_active_index = np.argmax(daily_totals)

print(f"\nMost Active Day: {days[most_active_index]} ({daily_totals[most_active_index]} steps)")