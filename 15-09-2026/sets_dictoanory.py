# # Set

# numbers = [10, 20, 20, 30, 40, 40, 50, 50]

# number = set(numbers)

# print(number)

# number_list = list(number)

# print(number_list)

# # Set add() and remove()

# skills = {"Python", "SQL", "Excel"}

# skills.add("Machine Learning")
# print(skills)

# skills.remove("Excel")
# print(skills)


# # Set Intersection

# python_students = {"Rahul", "Amit", "Priya", "Karan"}
# ml_students = {"Priya", "Karan", "Neha", "Vivek"}

# same_students = python_students.intersection(ml_students)

# print(same_students)

# # Set Difference
# # find students who are learning Python but not ML.

# python_students = {"Rahul", "Amit", "Priya", "Karan"}
# ml_students = {"Priya", "Karan", "Neha", "Vivek"}

# only_python_student = python_students.difference(ml_students)

# print(only_python_student)

# # Dictionary

# # student = {
# #     "name": "Rahul",
# #     "age": 21,
# #     "city": "Ahmedabad",
# #     "course": "Python"
# # }

# # print(student["name"])
# # print(student["age"])
# # print(student["city"])
# # print(student["course"])

# # Add & Delete

# # student["marks"] = 85
# # student["grade"] = "A"

# # print(student)

# # student.update({"marks":85})
# # student.update({"grade":"A"})
# # print(student)

# # del student["age"]
# # print(student)


# # Dictionary Loop

# student = {
#     "name": "Rahul",
#     "age": 21,
#     "marks": 85
# }

# for students in student.keys():
#     print(f"{students}:{student[students]}")

# # items()

# for key, value in student.items():
#     print(key,":",value)


# Other Practice

marks = [78, 45, 89, 92, 56, 34, 67, 89, 78, 90]

print("Number of Students:",len(marks))
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
print("Sorted Marks:",sorted(marks))

unique_marks = set(marks)
print("Unique Marks:",unique_marks)

# Student Records as Dictionary

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Ahmedabad",
    "python": 85,
    "sql": 78,
    "ml": 90
}

# del student["age"]
# del student["city"]
# print(student)

# del student["name"]
# new_list = []

# for i in student.values():
#     new_list.append(i)
# print(new_list)

# sum_list = sum(new_list)
# print(sum_list)

# avrage_list = sum_list/len(new_list)
# print(f"{avrage_list:.2f}")


print("Name:",student["name"])
print("Python:",student["python"])
print("SQL:",student["sql"])
print("ML:",student["ml"])

marks = []

for key,value in student.items():
    if key == "python" or key == "sql" or key == "ml":
        marks.append(value)

sum_marks = sum(marks)
avrage = sum_marks/len(marks)

print(f"avrage:{avrage:.2f}")

# Create a list containing only the numerical values:

person = {
    "age": 25,
    "experience": 2,
    "salary": 35000,
    "city": "Ahmedabad"
}

number_values = []

for value in person.values():
    if type(value) == int:
        number_values.append(value)
    
print(number_values)