def cal_average(students):
    total=0
    for marks in students.values():
        total+=marks
    return total/len(students)

def topper_student(students):
    topper=""
    max_marks=0
    for name,marks in students.items():
        if marks>max_marks:
            max_marks=marks
            topper=name
    return topper

def failed_student(students):
    failed=[]
    for name,marks in students.items():
        if marks<50:
            failed.append(name)
    return failed

# main data 
students={
    "Rahul": 78,
    "Amit": 45,
    "Priya": 89,
    "Neha": 67
}

# function call 
average=cal_average(students)
topper=topper_student(students)
failed=failed_student(students)

# output
print("Student Report")
print("----------------------")
print("topper : ",topper)
print("Average : ",average)
print("Failed Student : ",failed)


