students = [(81, "David", 19), (143, "Sam", 18), (111, "Gita", 21)]
roll_no , name , age = [] , [] , []

for student in students: roll_no.append(student[0]) , name.append(student[1]) , age.append(student[2])

print("Roll Numbers:", roll_no)
print("Names:", name)
print("Ages:", age)