import pandas as pd
import numpy as np

data = {
    "Name": ["Madhavi", "Anu", "Ravi", "Sita", "Kiran"],
    "Marks": [78, 65, 92, 35, 48]
}

df = pd.DataFrame(data)

print("Student Marks:")
print(df)

print("\nAverage Marks:", np.mean(df["Marks"]))
print("Highest Marks:", np.max(df["Marks"]))
print("Lowest Marks:", np.min(df["Marks"]))

print("\nPass Students:")
print(df[df["Marks"] >= 40])