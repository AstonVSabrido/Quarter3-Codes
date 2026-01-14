import numpy as np

names = ["Jane", "Marvoun", "Aston"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 6100, 4800, 5000, 5300],  # Jane
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6700]   # Aston
])

for i in range(len(names)):
    total_steps = np.sum(steps[i])
    average_steps = np.mean(steps[i])
    min_steps = np.min(steps[i])
    max_steps = np.max(steps[i])
    print(
        f"{names[i]} - Total Steps: {total_steps} | "
        f"Average: {average_steps:.1f} | Min: {min_steps} | Max: {max_steps}"
    )