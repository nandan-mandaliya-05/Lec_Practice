# % Formatting

name =  "Amit"
city = "Rajkot"
age = 22

print("My name is %s, I live in %s and I am %d years old" % (name,city,age))

# Float Formatting

price = 125.6789

print(f"Price: {price:.2f}")
print(f"Price: {price:.3f}")


# String Case

text = "python programming is very intersting"

print("Original:",text)
print("Upper:",text.upper())
print("lower:",text.lower())
print("title:",text.title())
print("capitalize:",text.capitalize())
print("swapcase:",text.swapcase())

# Find Position

sentence = "Python is a powerful programming language"

print("Pwerful Position: ",sentence.find("powerful"))

# Check String Exists

sentence = "Machine Learning is a part of Artificial Intelligence"

print("Machine exist:","Machine" in sentence)
print("Learning exist:","Learning" in sentence)
print("Python exist:","Python" in sentence)
print("Intelligence exist:","Intelligence" in sentence)

# startswith() and endswith()
filename = "python_programming.py"
print(filename.startswith("python"))
print(filename.endswith(".py"))
print(filename.endswith(".txt"))

# Replace

sentence = "I like Java. Java is easy to learn."
new_sentence = sentence.replace("Java","Python")
print(new_sentence)

# Replace Only Once
sentence = "Java is popular. Java is powerful. Java is everywhere."
print(sentence.replace("Java","Python",1))
print(sentence.replace("Java","Python",2))

# Count
data = "python is easy and python is powerful and python is popular"

print("Python count: ",data.count("python"))
print("is count: ",data.count("is"))
print("p count: ",data.count("p"))
print("java count: ",data.count("java"))

# Split Using Comma
fruits = "apple,banana,mango,grapes,orange"
fruit_list = fruits.split(",")
print(fruit_list)                       

# Split Sentence
sentence = "Python is easy to learn"
sentence_list = sentence.split(" ")
for i in sentence_list:
    print(i)
    
# Multiline String
languages = """Python
Java
JavaScript
C++
C#"""

language_list = languages.split("\n")
print(language_list)

# Combined Challenge

sentence = "Python Python is an easy programming language"

print("Original:",sentence)
print("Upper:",sentence.upper())
print("Title:",sentence.title())
print("easy position:",sentence.find("easy"))
print("Python Exist:","Python" in sentence)
print("Python count:",sentence.count("Python"))
print(sentence.replace("Python","Java"))
print(sentence.replace("Python","C++",1))

new_sentence = sentence.split(" ")
print(new_sentence)
for i in new_sentence:
    print(i)
    
# Mini Challenge
name = "Rahul"
skill = "Python"
city = "Ahmedabad"
experience = 2

print("Name: %s" % (name))
print("skill: %s" % (skill))
print("city: %s" % (city))
print("Experience: %d" % (experience))

print("%s is learning %s in %s." % (name,skill,city))
print("%s is learning %s in %s." % (name.upper(),skill.upper(),city.upper()))
print("%s is learning %s in %s." % (name.lower(),skill.lower(),city.lower()))
print("%s is learning %s in %s." % (name.title(),skill.title(),city.title()))

new_sentence = "%s is learning %s in %s." % (name,skill,city)
print(new_sentence)
print("Python exist:","Python" in new_sentence)
print("Python Position:",new_sentence.find("Python"))
print(new_sentence.replace("Python","Java"))

