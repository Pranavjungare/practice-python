students= {
    "Rahul": 78,
    "Amit": 45,
    "Priya": 89,
    "Neha": 67
}

total= 0
topper = ""
max_marks = 0
failed_student=[]

for name,marks in students.items():
    total += max_marks

    if marks > max_marks:
        max_marks = marks
        topper = name
    
    if marks< 50:
        failed_student.append(name)

average= total/ len(students)

print("\n Student Report")
print("---------------------")
print("Topper : ",topper)
print("Average : ",average)
print("Failed Student : ",failed_student)






