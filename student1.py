
import numpy as np
import pandas as pd

# Generate student data
np.random.seed(42)
n = 5000

student_id = np.arange(1, n + 1)
names = [f"Student_{i:04d}" for i in student_id]
ages = np.random.randint(18, 24, n)
attendance = np.round(np.random.uniform(45, 100, n), 2)

# Generate marks
python_marks = np.random.randint(20, 101, n)
math_marks = np.random.randint(20, 101, n)
database_marks = np.random.randint(20, 101, n)
english_marks = np.random.randint(20, 101, n)

# Calculate total and percentage
total_marks = (
    python_marks + math_marks +
    database_marks + english_marks
)

percentage = np.round(total_marks / 4, 2)

# Calculate result
result = np.where(
    (percentage >= 40) & (attendance >= 60),
    "Pass", "Fail"
)

# Create DataFrame
df = pd.DataFrame({
    "Student_ID": student_id,
    "Name": names,
    "Age": ages,
    "Attendance": attendance,
    "Python_Marks": python_marks,
    "Math_Marks": math_marks,
    "Database_Marks": database_marks,
    "English_Marks": english_marks,
    "Total_Marks": total_marks,
    "Percentage": percentage,
    "Result": result
})

# Save dataset
df.to_csv("student_performance_dataset.csv", index=False)

# Display first 5 students
print("\nFirst 5 Students:")
print(df.head())

# Dataset information
print("\nTotal Students:", len(df))
print("Total Columns:", len(df.columns))

# Average marks
print("\nAverage Marks:")
print("Python:", round(np.mean(python_marks), 2))
print("Math:", round(np.mean(math_marks), 2))
print("Database:", round(np.mean(database_marks), 2))
print("English:", round(np.mean(english_marks), 2))

# Overall statistics
print("\nOverall Statistics:")
print("Average Percentage:", round(np.mean(percentage), 2))
print("Highest Percentage:", np.max(percentage))
print("Lowest Percentage:", np.min(percentage))
print("Median Percentage:", np.median(percentage))

# Pass and fail count
print("\nPass/Fail Report:")
print(df["Result"].value_counts())

# Top 10 students
print("\nTop 10 Students:")
print(df.sort_values(
    by="Percentage", ascending=False
)[["Student_ID", "Name", "Percentage", "Result"]].head(10))

# Students with attendance >= 75%
print("\nAttendance >= 75%:")
print(df[df["Attendance"] >= 75].head(10))

# Passed students
print("\nPassed Students:")
print(df[df["Result"] == "Pass"].head(10))

# Failed students
print("\nFailed Students:")
print(df[df["Result"] == "Fail"].head(10))

print("\nDataset saved successfully!")

