# lambda_with_sorted.py

students = [("Adina", 90), ("Ali", 75), ("Dana", 85)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
