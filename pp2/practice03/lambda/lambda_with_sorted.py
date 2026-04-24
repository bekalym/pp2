#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
sorted_students_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students_desc)

#3
sorted_students_name = sorted(students, key=lambda x: x[0])
print(sorted_students_name)

#4
sorted_students_age = sorted(students, key=lambda x: x[1])
print(sorted_students_age)

#5
sorted_students_age_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students_age_desc)
