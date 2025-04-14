
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess data
path = "C:\\Users\\Bhargav sai\\Downloads\\_Kids_In_Motion__Playground_Programming__2016_to_2021 (2).csv"
data = pd.read_csv(path)

# Convert dates
data['Start_Date'] = pd.to_datetime(data['Week Start Date'])
data['End_Date'] = pd.to_datetime(data['Week End date'])

# Extract year and month
data['Year'] = data['Start_Date'].dt.year
data['Month'] = data['Start_Date'].dt.month

# Objective 1: Total Attendance Per Year
data.groupby('Year')['Total Attendance'].sum().plot(
    kind='line', marker='o', color='blue', figsize=(10, 6), title="Total Attendance Per Year"
)
plt.xlabel("Year")
plt.ylabel("Total Attendance")
plt.grid(True)
plt.tight_layout()
plt.show()
