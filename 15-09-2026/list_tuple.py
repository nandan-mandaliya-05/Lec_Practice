# # Level 1

# # List append()

# numbers = [10, 20, 30, 40]

# numbers.append(50)
# numbers.append(60)
# print(numbers)

# # List pop()

# numbers = [10, 20, 30, 40, 50]

# numbers.pop(0)
# numbers.pop()
# print(numbers)

# # List insert()

# languages = ["Python", "Java", "C++"]

# languages.insert(1,"Sql")
# print(languages)


# # List remove()

# languages = ["Python", "Java", "C++", "Python", "R"]

# # languages.remove("Java")
# # print(languages)

# languages.pop(1)
# print(languages)

# # count() and index()

# numbers = [10, 20, 10, 30, 10, 40]

# print(numbers.count(10))
# print(numbers.index(30))


# # Level 2 — List Comprehension


# # Square

# square_value = [number ** 2 for number in range(1,20)]
# print(square_value)


# # Even Numbers

# numbers = list(range(1,20))
# even_values  =  [number for number in numbers if number % 2==0 ]
# print(even_values)


# # Create a new list containing only marks greater than or equal to 50.

# # marks = [45, 67, 89, 32, 76, 91, 55, 28]

# # new_list = []

# # for mark in marks:
# #     if mark >= 50:
# #         new_list.append(mark)

# # print(new_list)

# marks = [45, 67, 89, 32, 76, 91, 55, 28]

# new_list = [mark for mark in marks if mark >= 50]

# print(new_list)

# # Tuple

# # student = ("Rahul", 21, "Ahmedabad", "Python")

# # print(student[0])
# # print(student[1])
# # print(student[2])
# # print(student[3])

# # numbers = (10, 20, 10, 30, 40, 10, 50)

# # print(numbers.count(10))
# # print(numbers.index(30))

# # numbers = (10, 20, 30)
# # numbers[0] = 100
# # print(numbers)



