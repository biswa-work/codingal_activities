# Activity 1: Get Rid of the Duplicates

student_data = {
    101: {"name": "Aarav", "class": 5, "subject": "Python"},
    102: {"name": "Mia", "class": 5, "subject": "Math"},
    103: {"name": "Aarav", "class": 5, "subject": "Python"},
    104: {"name": "Riya", "class": 6, "subject": "Science"}
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (
        details["name"],
        details["class"],
        details["subject"]
    )

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

print("Unique student records:")

for student_id, details in result.items():
    print(student_id, details)
