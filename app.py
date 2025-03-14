students = []
def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"


while True:
    print("\nEnter student details:")
    name = input("Student Name: ")
    roll_number = input("Roll Number: ")

    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                marks[subject] = float(input(f"{subject} Marks: "))
                if 0 <= marks[subject] <= 100:
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input! Enter numeric marks.")

    total_marks = sum(marks.values())
    percentage = total_marks / len(subjects)
    grade = calculate_grade(percentage)

    students.append({
        "Name": name,
        "Roll Number": roll_number,
        "Marks": marks,
        "Total": total_marks,
        "Percentage": percentage,
        "Grade": grade
    })

    print(f"\nRecord of {name} inserted successfully.")
    more = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().upper()
    if more != 'Y':
        break

print("\nStudent Report Cards:")
for student in students:
    print("\n--------------------------------")
    print(f"Name: {student['Name']}")
    print(f"Roll Number: {student['Roll Number']}")
    for subject, mark in student["Marks"].items():
        print(f"{subject}: {mark}")
    print(f"Total Marks: {student['Total']}/500")
    print(f"Percentage: {student['Percentage']}%")
    print(f"Grade: {student['Grade']}")
    print("--------------------------------")
