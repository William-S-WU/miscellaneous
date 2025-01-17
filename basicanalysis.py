import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('combined.csv')

print("Column Names:")
print(df.columns)
print("\nBasic Info:")
print(df.info())

# Plot histograms for all columns
df.hist(figsize=(12, 10), bins=20)
plt.suptitle('Histograms for All Columns')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to fit the title
plt.show()
