
# Creating String
name = "Karan"
destination = "Junagadh"

print(name)
print(destination)

# spam_message = """Buy Now
# Dm me
# Order this Product
# """
spam_message = '''Buy Now
Dm me
Order this Product
'''

print(spam_message)

# string indexing

sr = "United States"

print(sr[1:5]) # nite

print(sr[0:]) # United States
print(sr[2:6]) # ited
print(sr[:]) # United States

print(sr[:13]) # United States # Positive indexing
print(sr[:-1]) # United State # This called nagative indexing
print(sr[-6:-1]) # State 
print(sr[-13:]) # United States
     
    # By steps indexing     
print(sr[::2]) # Uie tts

    # Reverse String
print(sr[::-1]) # setats detinU

# String concatinating

name =  "Lakhan"
surname = "Ravrani"
print(name + " "+ surname)
print(f"{name} {surname}")


# f-string
name = "karan"
age = 25

print(f"{name} is a able to drive car beacuse his age is {age}.")

# decimal places

height = 5.6
print(f"{name} height is {height:.2f}")

# Expressation inside  F-STRING

a = 10
b = 5

print(f"Divition = {a/b}")

# format() Method

print("{} is a able to drive car beacuse his age is {}.".format(name,age))

# Positional arguments
print("{1} is a able to drive car beacuse his age is {0}.".format(name,age))
print("{0} is a able to drive car beacuse his age is {1}.".format(name,age))

# named arguments
print("{n} is a able to drive car beacuse his age is {a}.".format(n = name,a = age))

