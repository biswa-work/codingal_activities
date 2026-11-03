# Activity 3: Student Marks

def calculate_average(marks):
    return sum(marks) / len(marks)

students = ["Aarav", "Mia", "Riya"]
marks = [85, 92, 78]

student_reports = list(zip(students, marks))

for name, score in student_reports:
    print(name, "scored", score)

average = calculate_average(marks)
print("Class average:", average)

passed = [
    name for name, score in student_reports
    if score >= 40
]

print("Students who passed:", passed)
