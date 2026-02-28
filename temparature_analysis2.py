import numpy as np
scores = np.array([85,90,78,92,88,76,95,82,89,91,87,84])
print(scores)
print(scores.shape)
print("Total Elements", scores.size)
print("Highest Score:", scores.max())
print("Lowest Score:", scores.min())
print("Range:", scores.max() - scores.min())