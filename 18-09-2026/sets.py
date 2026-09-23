students = [
    {
        "id": 101,
        "name": " Rahul ",
        "city": "Ahmedabad",
        "skills": ["Python", "SQL"],
        "scores": [85, 90, 78]
    },
    {
        "id": 102,
        "name": "Priya",
        "city": "Surat",
        "skills": ["Python", "Excel"],
        "scores": [92, 88, 95]
    },
    {
        "id": 103,
        "name": " AMIT ",
        "city": "Ahmedabad",
        "skills": ["Java", "SQL"],
        "scores": [65, 72, 68]
    }
]

# 1. Clean names

# Remove extra spaces with strip()
# Convert names to title case.

# 2. Display student names
for student in students:
    student["name"] = student["name"].strip().title()
    print(student["name"])

# 3. Calculate total and average score

# Store total and average in each student's dictionary.

for student in students:
    sum_score = 0
    
    for score in student["scores"]:
        sum_score += score
    
    avarage = (sum_score / len(student["scores"]))
    
    print("Name:", student["name"])
    print("Total:", sum_score)
    print("Avarage:",avarage)
    student["total"]  = sum_score
    student["avarage"] = avarage
    
for student in students:
    print(student)

# 4. Grade students and Grade count

# >= 90 → A
# >= 80 → B
# >= 70 → C
# Otherwise → D

grade_count = {
    "A":0,
    "B":0,
    "C":0,
    "D":0
}
for student in students:
    
    avarage =  student["avarage"]
    
    if avarage >= 90:
        grade = "A"
    elif avarage >= 80:
        grade = "B"
    elif avarage >= 70:
        grade = "C"
    else:
        grade = "D"
        
    student["grade"] = grade
    grade_count[grade] += 1
    

for student in students:
    print(
        student["name"],
        "Total:", student["total"],
        "Avarage:",student["avarage"],
        "Grade:", student["grade"]  
    )
    
print("\nGrade Count:",grade_count)

# 5. Add new student

# new_student = {}

# for i in range(1):
#     new_student["id"] = int(input("Enter student ID: "))
#     new_student["name"] = input("Enter student name: ")
#     new_student["city"] = input("Enter student city: ")

#     skills = []
#     for i in range(2):
#         skill = input(f"Enter skill {i + 1}: ")
#         skills.append(skill)

#     new_student["skills"] = skills

#     scores = []
#     for i in range(3):
#         score = int(input(f"Enter score {i + 1}: "))
#         scores.append(score)

#     new_student["scores"] = scores

# students.append(new_student)

# print("\nstudent added successfully.")

# for student in students:
#     print(student)


# 6. Update an existing student's score

# student_id = int(input("Enter student ID:"))

# for student in students:
#     if student["id"] == student_id:
#         new_score = []
        
#         for i in range(len(student["scores"])):
#             score = int(input(f"Enter score {i + 1}: "))
#             new_score.append(score)
        
#         student["scores"] = new_score
        
#         print("Score updated successfully.")
#         break

# for student in students:
#     print(student)                 
        
# 7. Delete a student by ID  
  
# student_id = int(input("Enter student id you want to delete: "))

# for student in students:
#     if student["id"] == student_id:
#         students.remove(student)
#         print("student deleted successfully.")
#         break
# else:
#     print("Student ID not found.")
    
# print("\nUpdated students:")

# for student in students:
#     print(student)

#   8. Find students whose average is >= 75  

# for student in students:
#     if student["avarage"] >= 75:
#         print(student)

# 9. Find the highest-scoring student

# highest = students[0]

# for student in students:
#     if student["scores"] > highest["scores"]:
#     # if student["total"] > highest["total"]:
#         highest = student

# print(highest["scores"])
# print(highest["total"])
# print(highest["name"])


# 10. Sort students by average

students.sort(key=lambda x: x["avarage"], reverse=True)
print(students)

tuple_name = tuple()

for student in students:
    tuple_name += (student["name"],)
print(tuple_name)

# 12. Create a set of unique cities

unique_city = set()

for student in students:
    unique_city.add(student["city"])

print(unique_city)

# 13. Create a set of all unique skills

unique_skills = set()

for student in students:
    for skill in student["skills"]:
        unique_skills.add(skill)
    
print(unique_skills)

# 14. Convert the skills set into a list

set_lst_of_skills = list(unique_skills)
print(set_lst_of_skills)

# 15. List comprehension

# Create names of students whose average is >= 80:

high_avrage_Student = [student["name"] for student in students if student["avarage"] >= 80]

print(high_avrage_Student)


# 16. Student report card

# Print:

# Name: Priya
# City: Surat
# Skills: Python, Excel
# Total: 275
# Average: 91.67
# Grade: A

for student in students:
    print("Name:",student["name"])
    print("City:",student["city"])
    print("skills:",student["skills"])
    print("Total:",student["total"])
    print("Avarage",student["avarage"])
    print("Grade:",student["grade"])
    print()


# 17. Final Data Summary

# Now combine the information into one dictionary:

final_data_summary = {
   "total_students":len(students),
   "avarage_class_score":sum(student["avarage"]for student in students) /len(students),
   "highest_score" : 0,
   "unique_city" : unique_city,
   "unique_skills" : unique_skills
}

highest_scores = students[0]["avarage"]

for student in students:
    if student["avarage"] > highest_scores:
        highest_scores = student
        
print(highest_scores)

final_data_summary.update({"highest_scores":highest_scores})

for key , value in final_data_summary.items(): 
    print(key,":",value)
