students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Get unique grades and sort them
grades = sorted(set(student[1] for student in students))

# Get the second lowest grade
second_lowest_grade = grades[1]

# Find all students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Sort names alphabetically and print
second_lowest_students.sort()
for name in second_lowest_students:
    print(name)