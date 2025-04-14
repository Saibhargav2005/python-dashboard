# Objective 5: Program Duration vs Attendance
data['Program_Duration_Days'] = (data['End_Date'] - data['Start_Date']).dt.days

plt.figure(figsize=(10, 6))
plt.scatter(data['Program_Duration_Days'], data['Total Attendance'], alpha=0.6, color='teal')
plt.title("Program Duration vs Total Attendance")
plt.xlabel("Program Duration (in Days)")
plt.ylabel("Total Attendance")
plt.grid(True)
plt.tight_layout()
plt.show()
