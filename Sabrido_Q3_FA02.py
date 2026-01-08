import numpy as np

names = ["Jane", "Marvoun", "Aston"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 6100, 4800, 5000, 5300],  # Jane
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6700]   # Aston
])

# Display all step data
print("Daily steps (Monday to Friday):")
for i in range(len(names)):
    print(names[i], ":", steps[i])
