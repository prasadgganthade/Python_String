# Exercise 1A: Create a string made of the first, middle and last character
name ='Prasad'
name2 = 'James'
def name_middle(str):
    print('Original string :',str)
    # First character
    result = str[0]
    # middle character
    length = len(str)
    mid = int(length/2)
    result =result + str[mid]
    # last character
    result = result + str[-1]
    print(result)

name_middle(name)
name_middle(name2)
# Exercise 1B: Create a string made of the middle three characters

def middle_3_chr(str):
    print('Original String :',str)
    # First middle character
    mid = int(len(str)/2)
    # using string slicing to get result
    result = str[mid-1:mid+2]
    print('Midle 3 characters :',result)

middle_3_chr(name)
middle_3_chr(name2)

# Exercise 2: Append new string in the middle of a given string

def append_str_middle(string1,string2):
    print('Original string is :',string1)
    print('Original string 2 is :',string2)
    mid = int(len(string1)/2)
    result = string1[:mid] + string2 + string1[mid:]
    print(result)

append_str_middle('John','Don')

# Exercise 4: Arrange string characters such that lowercase letters should come first
str= 'PYNaTive'
print('original string :',str)
upper = []
lower = []
for i in str:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)

result = "".join(lower + upper)
print(result)

# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
alpha_count = 0
number_count = 0
special_char = 0

for i in str1:
    if i.isalpha():
        alpha_count = alpha_count + 1
    elif i.isdigit():
        number_count = number_count + 1
    else:
        special_char = special_char + 1
print('The character count is :',alpha_count)
print('The number count is :',number_count)
print('The special count is :',special_char)

# Exercise 7: String characters balance Test

def check_string(str1,str2):
    print('Original string 1 is :',str1)
    print('Original string 2 is :',str2)
    flag = True
    for char in str1:
        if char in str2:
            continue
        else:
            flag = False
    return flag
s1 = 'Py'
s2 = 'PYnative'
result = check_string(s1,s2)
if result == True:
    print('The string are balanced')
else:
    print('The strings are not balanced')

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
print(str1.count('USA'))

# Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
sum = 0
count = 0
for i in str1:
    if i.isdigit():
        sum = sum + int(i)
        count = count + 1
avg = sum / count
print('Average :',avg)
print(sum)

# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = 'Apple'
char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result :',char_dict)

# Exercise 11: Reverse a given string

str1 = 'Python'
print('Reverse of string is :',str1[::-1])
name = "".join(reversed(str1))
print(name)

# Exercise 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."

print('The last occurance of emma is',str1.rfind('Emma'))

# Exercise 13: Split a string on hyphens
str2 = 'John-is-data-scientist'
new = str2.split("-")
print(new)
for i in new:
    print(i)

# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print('The original list :',str_list)

new_list = []
for i in str_list:
    if i:
        new_list.append(i)

print('After removing empty strings')
print(new_list)
# method 2
new = list(filter(None,str_list))
print(new)

