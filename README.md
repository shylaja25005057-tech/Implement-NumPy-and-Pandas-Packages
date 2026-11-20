# Implement-NumPy-and-Pandas-Packages

Aim: To write a Python program to implement NumPy and Pandas packages.

Algorithm:

1.Start.

2.Import NumPy and Pandas libraries.

3.Create a NumPy array.

4.Perform mathematical operations.

5.Create a Pandas DataFrame.

6.Display the DataFrame.

7.Stop.

Source Code:

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
<img width="1167" height="801" alt="image" src="https://github.com/user-attachments/assets/863e7b72-16b5-4943-9fc3-5560dd5ecae0" />
