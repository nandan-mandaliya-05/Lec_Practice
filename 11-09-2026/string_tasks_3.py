# String JOIN

# words = ["Python","is","awasome"]

# word = " ".join(words)
# print(word)

# JOIN with comma

# words = ["Apple", "Banana", "Mango"]

# print(", ".join(words))

# result = ", ".join(words)
# print(result)

# Strip

# text = "     Hello Python     "
# print(len(text))
# print("strip length:",len(text.strip()))
# print("lstrip length:",len(text.lstrip()))
# print("rstrip length:",len(text.rstrip()))

# Strip the text

# text = "     Hello Python     "
# print(text.strip())

# Count alphabets

# text = "Python123@#"

# count = 0
# for i in text:
#     if i.isalpha():
#         count += 1
# print(f"Alphabets: {count}")

# Remove non-alphabetic characters

# text = "Hello123@Python!"

# new_text = ""
# for i in text:
#     if i.isalpha():
#         new_text += i

# print(new_text)

# Character checker

# any_word = input("Enter a any word latter and also number: ")

# print("\n-----Character information-----")
# print("Alphabet:",any_word.isalpha())
# print("Digit:",any_word.isdigit())
# print("Lower:",any_word.islower())
# print("Upper:",any_word.isupper())
# print("Space:",any_word.isspace())
    

#  Reverse a string

# sr = input("Enter a word: ")
        
#         #by join
# revers_text = "".join(reversed(sr))
# print(revers_text)
#         #by list
# rev_text_1 = list(sr)
# rev_text_1.reverse()
# print("".join(rev_text_1))
#         #by indexing
# print(sr[::-1])

# Palindrome checker

# st = input("Enter a String:")

# new_st = st[::-1]

# print(new_st)

# if new_st.lower()==st.lower():
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")


# Reverse each word

# text = "Python is awesome"

# words = text.split()

# reverse_words = []

# for word in words:
#     reverse_words.append(word[::-1])
    
# result = " ".join(reverse_words)

# print(result)


# Remove non-alphabets + reverse

# s = "Python123@"

# new_s = ""

# for i in s:
#     if i.isalpha():
#         new_s += i

# print(new_s[::-1])

# Palindrome after cleaning

# m = "Madam123@"

# m_new = ""

# rev_m_new = m_new[::-1]

# for i in m:
#     if i.isalpha():
#         m_new += i
        
# if m_new.lower() == rev_m_new.lower():
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    

# Sentence JOIN

# words = ["I", "am", "learning", "Python"]

# word_split = " ".join(words)

# print(word_split)

# word_split_list = word_split.split()

# print(word_split_list)

# Escape Character Practice

# print("Hello\nword")
# print("Python\tProgramming")
# print("She said \"Python is easy\"")
# print("it\'s Python")
# print("C:\\Python\\Projects")


# Final Mini Project

word = input("Enter a String:")

print("Original String:",word)

new_string = ""
for i in word:
    if i.isalpha():
        new_string += i
print("Clean String:",new_string)

rev_str = word[::-1]
print("Reversed String:",rev_str)

print("Is Palindrome:",rev_str == new_string)
# if rev_str == new_string:
#     print("Is Palindrome: Yes")
# else:
#     print("Is Palindrome: No")

num = 0
dig = 0
spc = 0
for i in word:    
    if i.isalpha():
        num += 1
    elif i.isdigit():
        dig += 1
    elif i.isspace():
        spc += 1
print("Number of Alphabet:",num)
print("Number of Digit:",dig)
print("Number of Space:",spc)