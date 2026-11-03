# Activity 2: Student Report

students = {
    "Aarav": [80, 90, 85],
    "Mia": [95, 88, 92],
    "Riya": [70, 75, 80]
}

for name, scores in students.items():
    average = sum(scores) / len(scores)

    print("\nStudent:", name)
    print("Marks:", scores)
    print("Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Needs Improvement")
