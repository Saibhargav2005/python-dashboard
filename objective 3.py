# Objective 3: Average Attendance by Day of Week
day_columns = [f"{day}'s Attendance" for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']]
data[day_columns].mean().plot(
    kind='bar', color='purple', figsize=(10, 6), title="Average Attendance by Day of the Week"
)
plt.ylabel("Average Attendance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
