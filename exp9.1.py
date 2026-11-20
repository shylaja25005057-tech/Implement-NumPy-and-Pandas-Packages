# Implement NumPy and Pandas

import numpy as np
import pandas as pd

# Create NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Create Pandas DataFrame
data = {
    "Name": ["Arun", "Bala", "Charan", "Divya"],
    "Marks": [65, 72, 90, 85],
    "Attendance": [90, 85, 95, 75]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nStudent Details:")
print(df.describe())
