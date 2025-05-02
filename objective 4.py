# Objective 4:Number of Programs Offered Per Year
data.groupby('Year').size().plot(
    kind='line', marker='o', color='red', figsize=(10, 6), title="Number of Programs Offered Each Year"
)
plt.xlabel("Year")
plt.ylabel("Number of Programs")
plt.grid(True)
plt.tight_layout()
plt.show()
