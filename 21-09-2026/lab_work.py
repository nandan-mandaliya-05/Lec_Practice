# Create a list of dictionaries to store student records such as:

students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

# 1. Print the name of each student using a loop.
for i in range(len(students)):
    print(f"{i + 1}. Student Name is",students[i]["name"])

# for student in students:
#     print(student["name"])

# 2. Print the average score of all students.

total = 0

for student in students:
    total += student["score"]
    
# print(total)
average = total/len(students)
print("Average of All Students are",average,"and Total is",total)

# 3. Add a new student record to the list

# new_student = {}

# for i in range(1):
#     new_student["id"] = int(input("Enter a ID:"))
#     new_student["name"] = input("Enter a name:")
#     new_student["score"] = int(input("Enter a score:"))
    
# students.append(new_student)

# for student in students:
#     print(student)
    
# 4. Update the score of a student with ID 102 to 88.

# student_id = int(input("Enter a ID: "))

# for student in students:
#     if student["id"] == student_id:
#         score = int(input(f"Update a score of id {student_id}: "))
#         student["score"] = score
        
# print("\nStudent score Updated Successfully.")

# for student in students:
#     print(student)
    
# 5. Delete the record of the student named "Charlie".

# for student in students:
#     if student["name"] == "Charlie":
#         students.remove(student)
        
# for student in students:
#     print(students)

# 6. Print names of students who scored more than 80.

print("This is students names scored more than 80.")

for student in students:
    if student["score"] > 80:
        print(student["name"])

# 7. Sort the list of students by score (descending).

students.sort(key=lambda x: x["score"], reverse=True)
print(students)

# 8. Find the student with the highest score.

highest = students[0]

for student in students:
    if student["score"] > highest["score"]:
        highest = student
        
print("Highest Score Student name is",highest["name"],"\nHighest Score is",highest["score"])

# 9. Use a loop to create a report in this format:
#    Name: Alice | Score: 85 | Grade: B
#    (Add grading logic: A = 90+, B = 80–89, C = <80)

for student in students:
    if student["score"] > 90:
        grade = "A"
    elif student["score"] > 80 and student["score"] < 89:
        grade = "B"
    elif student["score"] < 80:
        grade = "c"
    
    student["Grade:"] = grade
    print("Name:",student["name"],"|","Score:",student["score"],"|","Grade:",grade)
 
 
# 10. Count how many students got each grade.
   
grade_count = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
}

for student in students:
    if student["score"] > 90:
        grade = "A"
    elif student["score"] > 80 and student["score"] < 89:
        grade = "B"
    elif student["score"] < 80:
        grade = "C"
        
    grade_count[grade] += 1

for key,value in grade_count.items():
    print(key,":",value)
    
