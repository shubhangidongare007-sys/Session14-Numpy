import numpy as np

arr = np.random.randint(20, 81, (4,5))

print(arr)

print("Minimum:", arr.min())
print("Maximum:", arr.max())

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())

print("Row Sum:", arr.sum(axis=1))
print("Column Sum:", arr.sum(axis=0))