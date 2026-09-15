# List Creation & Access

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

print(colors)
print(colors[0])
print(colors[4])
print(colors[1])
print(colors[3])


# List Loop

print("="*40)

animals = ["Dog", "Cat", "Lion", "Tiger", "Horse"]

for animal in animals:
    print(animal)
    
    
# Add Values

print("="*40)

students = ["Rahul", "Amit", "Priya"]

students.append("Nandan")
students.append("Karan")

print(students)


# Remove Values
print("="*40)

numbers = [10, 20, 30, 40, 50]

numbers.pop(0)
numbers.pop()
print(numbers)

# Sorting
print("="*40)

marks = [45, 89, 23, 67, 12, 95]

print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)


# Tuple
print("="*40)

numbers = (10, 20, 30, 40, 50)

print(numbers)
print(numbers[0])
print(numbers[4])
print(numbers[2])

for num in numbers:
    print(num)
    
    
# List vs Tuple
print("="*40)

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

my_list[0] = 100
print(my_list)

# my_tuple[0] = 100
# print(my_tuple)


# Mixed Challenge
print("="*40)

fruits = ["Mango", "Apple", "Banana", "Orange"]

print(fruits)

fruits.append("Grapes")
print(fruits)

fruits.pop(1)
print(fruits)

print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

for fruit in fruits:
    print(fruit)