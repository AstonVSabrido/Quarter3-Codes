import numpy as np

names = ["Jane", "Marvoun", "Aston"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 6100, 4800, 5000, 5300],  # Jane
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6700]   # Aston
])

total_steps = np.sum(steps, axis=1)

max_index = np.argmax(total_steps)
min_index = np.argmin(total_steps)

print("Total steps per person:")
for i in range(len(names)):
    print(f"{names[i]}: {total_steps[i]} steps")

print(f"\nPerson with the highest total steps: {names[max_index]} ({total_steps[max_index]} steps)")

difference = total_steps[max_index] - total_steps[min_index]
print(f"Difference between highest and lowest total steps: {difference} steps")
