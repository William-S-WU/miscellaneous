import os
import pandas as pd

#print("Current working directory:", os.getcwd()) #use to find current directory
directory = os.getcwd()  #replace if working directory is not disired directory

# List to hold individual DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the CSV file
        df = pd.read_csv(os.path.join(directory, filename))
        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df.to_csv("combined.csv", index=False)

print("All CSV files have been combined into a single DataFrame.")

