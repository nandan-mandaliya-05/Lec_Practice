# Set Operations
# 
# numbers = {10, 20, 20, 30, 40, 40, 50}

# print(f"Numbers: {numbers}")

# numbers.add(90)
# print(numbers)

# numbers.remove(20)
# print(numbers)
# print(f"30 is Exist in numbers:",30 in numbers)

# set_lst = list(numbers)
# print(set_lst)

# Remove Duplicates

# numbers = [10, 20, 20, 30, 40, 40, 50, 50, 60]

# num_lst = set(numbers)
# print(num_lst)

# Dictionary Operations

# student = {
#     "name": "Rahul",
#     "age": 21,
#     "marks": 85
# }

# print(f"Student name is",student["name"])

# student["city"] = "Ahmedabad"
# print(student)

# for i in student:
#     if student["marks"] == 85:
#         student["marks"] = 90
    
# print(student)

# student["marks"] = 90
# print(student)

# del student["age"]
# print(student)

# for key in student.keys():
#     print(key)
    
# for value in student.values():
#     print(value)
    
# for key,value in student.items():
#     print(f"{key} : {value}")

# Dictionary From Lists

# keys = ["id", "name", "city", "salary"]
# values = [101, "Amit", "Surat", 45000]

# employee = {}

# for i in range(len(keys)):
#     employee[keys[i]] = values[i]
    
# print(employee)


# Type Conversion

# numbers = [10, 20, 20, 30, 40, 40, 50]

# print("Original List:",numbers)

# new_set = set(numbers)
# print("Set:",new_set)
# # print("Set:",set(numbers))

# new_list =  list(new_set)
# print("New List:",new_list)

# print("Tuple:",tuple(new_list))

# Delete List Items

# numbers = [10, 20, 30, 40, 50, 60]  

# del numbers[2]
# del numbers[4]
# print(numbers)

# Student Management System

# students = [
#     {"id": 101, "name": "Priya", "score": 85},
#     {"id": 102, "name": "Pooja", "score": 75},
#     {"id": 103, "name": "Rahul", "score": 89},
#     {"id": 104, "name": "Amit", "score": 62},
#     {"id": 105, "name": "Neha", "score": 95}
# ]

# # Part A — Display Data

# for i in students:
#     print(i["name"])
# print("\n",end = "")

# # Part B — Pass Students

# for i in students:
#     if i["score"] >= 70:
#         print(i["name"])
# print("\n",end = "")

# # Part C — Highest Score

# highest = students[0]

# for student in students:
#     if student["score"] > highest["score"]:
#         highest = student
# print("Highest Score Student:",highest["name"])
# print("Highest Score:",highest["score"])
# print("\n",end = "")

# # Part D — Extract Scores

# scores = [85, 75, 89, 62, 95]

# for i in scores:
#     print(i)
# print("\n",end = "")
    
# # Part E — Unique Scores

# score_set = set(scores)
# print(score_set)
# print("\n",end = "")

# set_lt = list(score_set)
# print(set_lt)
# print("\n",end = "")

# # Part F — Add Information

# for i in range(len(students)):
#     print(f"{i + 1}",students[i])
#     # name = students[i]["name"]
#     add_city = input(f"Enter a city to you want to add in {students[i]['name']}: ")
#     students[i]["city"] = add_city
#     print(f"index {i + 1} {students[i]['name']} in city add Succesfully...\n")
    
# print("This is all students details with city..\n")

# for i in students:
#     print(i)
# print("\n",end = "")  

# # Part G — Delete Information
# for student in students:
#      del student["id"]

# for idx in students:
#     print(idx)
# print("\n",end = "") 

# # Part H — Final Output

# for index in range(len(students)):
#     name = students[index]["name"]
#     score = students[index]["score"]
#     city = students[index]["city"]
#     print(f"{name} : {score} : {city}")


# Mini Data Analysis Exercise

employees = [
    {"id": 101, "name": "Rahul", "department": "IT", "salary": 45000},
    {"id": 102, "name": "Amit", "department": "Data", "salary": 55000},
    {"id": 103, "name": "Priya", "department": "AI", "salary": 65000},
    {"id": 104, "name": "Neha", "department": "IT", "salary": 45000},
    {"id": 105, "name": "Karan", "department": "Data", "salary": 60000}
]

# for employee in employees:
#     print(employee["name"])
# print("="* 40)


# for employee in employees:
#     if employee["salary"] >= 50000:
#         print(employee)

# lst = []

# for employee in employees:
#     lst.append(employee["salary"])
# print(lst)

# highest_salary = employees[0]

# for employee in employees:
#     if employee["salary"] > highest_salary["salary"]:
#         highest_salary = employee
# print("Highest Salary Student:",highest_salary["name"])
# print("Highest Salary:", highest_salary["salary"])

# department_set = set()

# for employee in employees:
#     department_set.add(employee["department"])
# print(department_set)


# department_set_list = list(department_set)
# print(department_set_list)

# Add "experience" to every employee.

# for index in range(len(employees)):
#     experience = int(input(f"{index + 1}. {employees[index]['name']} How many years experince in {employees[index]['department']} : "))
#     employees[index]["experience"] = experience
#     print("Experience added Sucessfully.")

# print("This is a Employee list with Experience.")
# for employee in employees:
#     print(employee)

# for employee in employees:
#     del employee["id"]
#     print(employee)
    
for employee in employees:
    print("\nEmployee Details:")
    
    for key,value in employee.items():
        print(key,":",value)
      