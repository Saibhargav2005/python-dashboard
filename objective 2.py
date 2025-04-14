# Objective 2: Average Monthly Attendance Trend
data.groupby('Month')['Total Attendance'].mean().plot(
    kind='bar', color='orange', figsize=(10, 6), title="Average Monthly Attendance"
)
plt.xlabel("Month")
plt.ylabel("Average Attendance")
plt.xticks(
    ticks=range(12),
    labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    rotation=45
)
plt.tight_layout()
plt.show()
