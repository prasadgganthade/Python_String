# """
# # representation of string
# # using single quotes
# text = 'geeksfor geeks'
# text1 = "Geeksfor geeks"
# print(text)
# print(text1)
# # creating a string
# String1 = 'Welcome to the geeks world'
# print(String1)
# String2 = "Welcome to pandas"
# print(String2)
# String3 = """#My name is Prasad Ganthade
# #I live in Belgaum.
# #My state is Karnataka"""
# # print(String3)
# # # Accessing the character in the string
# # print(String1[0])
# # # last character
# # print(String1[-1])
# # # reversing a string
# # print(String1[::-1])
# # print(text)
# # reverse the text using join and reversed function
# #gfg = "".join(reversed(text))
# #print(gfg)
# # String Slicing
# """
# #To access a range of characters in the string , slicing method is used.
# #It is done by slicing operator colon(:)
# -----------------------------------------------------
# =====================================================
# METHODS OF STRING
# =================================================
# ------------------------------------------------------
# """
# # 1. convert letter into uppercase
# s = 'welcome to the batch 21'
# s.upper()
# print(s.upper())
# a = 'my name is prasad ganthade'
# print(a.upper())
# #2. covert letter into lowercase
# b = 'I LIVE IN BELAGAVI'
# print(b.lower())
# c = 'I love INDia'
# print(c.lower())
# #3 Capitalize : make first letter of first work in CAPS
# print(a.capitalize())
# print(s.capitalize())
# #4. Title : Returns the version of strings where word stats with uppercase rest characters are lower case
# print(s.title())
# print(a.title())
# # 5 index : It returns lowest index
# print(s.index('21'))
# print(s.index('to'))
# # 6 rindex : find out highest index
# print(s.rindex('t'))
# # 7 find(): It also gives an index of an element
# print(s.find('b'))
# print(s.find('batch'))
# #print(s.index('tom'))
# print(s.find('tom'))
# # 8 split(): used to convert string to list
# print(s.split())
# name = 'ramesh, ganesh, mahesh, nagesh'
# print(name.split(','))
# log = '125-568-895-861'
# print(log.split('-'))
# s_name = 'ganthade*prasad*ganesh*gayatri'
# print(s_name.split('*'))
# # 9. strip() : used to remove space
# r = '        ganesh      '
# print(r.strip())
# m = '********ganesh******'
# print(m.strip('*'))
# # lstrip() : remove left side spaces
# m = '        gayatri      '
# print(m.lstrip())
# m = '88888888mahesh88888'
# print(m.lstrip('8'))
# #rstrip() : remove right side spaces
# p = '     prasad      '
# print(p.rstrip())
# p = '4444444prasad44444'
# print(p.rstrip('4'))
# # 10. replace(): in order to remove an element present in between
# # a.replace(old,new)
# print(p.replace('4',''))
# f = '*#*abhishek'
# print(f.replace('*#*',''))
# #11. concanating two strings
# f_name = 'prasad'
# l_name = 'ganthade'
# full_name = f_name + " " + l_name
# print(full_name)
# v = 'abhishek'
# v_ = v[:4]+ ' ' + v[4:]
# print(v_)
# print(s)
# # 12. count() : number of occurances
# print(s.count('e'))
# print(s.count('t'))
# print(s.count('PQ'))
# print(s.count('the'))
# #13. join(): used to convert list to string
# print(name)
# result = name.split(',')
# print(result)
# joined = ''.join(result)
# print(joined)
# k = ['gangadhar ', 'hi','shaktiman','hai']
# print(' '.join(k))
# s1 = 'python'
# print(s1)
# t = 'i love my india'
# #14. startswith() : It give a boolean output
# print(t.startswith('i'))
# print(t.startswith('m'))
# # 15. endswith() : it gives output in the boolean form
# print(t.endswith('india'))
# print(t.endswith('my'))
# print(t.endswith('a'))
# # 15. isalpha() : it check whether string is alphabatic or not & gives output in the form of boolean
# x = 'abc'
# print()
# print(x.isalpha())
# print(p.isalpha())
# print(p.isalnum())
# # 16. alnum() : its check whether the string is alphbatic and numeric and gives output in the form of boolean
# print(x.isalnum())
# print(s.isalnum())
# y= 'pqr'
# print()
# print(y.isalnum())
# print(s)
# print(s.isalnum())
# print(p.isdigit())
# string problems Python app
#1
"""
name = input('Enter the aname which has atleast one a letter: ')
name = name.lower()
replaced_name = name.replace('a','$')
print('Modified string:',replaced_name)
2 - Python programme to remove nth index of character of string
string = input('Enter the details: ')
def remove(string,n):
    first = string[:n]
    last = string[n+1:]
    return first + last
n = int(input('Enter the character number to be removerd from string: '))
print('Modified string:',remove(string,n))
print('The character removed whose index is',n)
--------------------------------------------------
3. python programme for to detect if two strings are "Anagrams"
str1 = input('Enter 1st string : ')
str2 = input('Enter 2nd string : ')
if sorted(str1) == sorted(str2):
    print('Given string is anagram')
else:
    print('Given string is not anagram')
------------------------------------------------------------
4. write a python programme for to form new string where first and last character have been exchanged
str = input('Enter the string : ')
def change(str):
    return str[-1:] + str[1:-1] +str[0]
print(change(str))
--------------------------------------------------------------
5. To count the number of vowels of string
str = input('Enter the word : ')
vowels = 0
for i in str:
    if (i=='a' or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
        vowels = vowels + 1
print('Number of vowels are',vowels)
------------------------------------------------------------------
6. Take a string and replace every black space with hyphen
str = 'I love coutry too much'
d = str.replace(' ','-')
print(d)
------------------------------------------------------------------
7. Calculate the length of string without using a libraray function
str = input('Enter the string : ')
count = 0
for i in str:
    count = count + 1
print('The length of string is',count)
---------------------------------------------------------------------
8. Remove the characters of odd index values in a string
str = input('Enter the string : ')
name = ""
for i in range(len(str)):
    if i % 2 == 0:
        name = name + str[i]
print('Modified string:',name)
------------------------------------------------------------------------
9. Calculate the number of words and the number of characters
string = input('Enter sentence : ')
word = 1
char = 0
for i in string:
    char = char + 1
    if (i == ' '):
        word = word + 1
print('The number of words are',word)
print('The number of characters are',char)
------------------------------------------------------
10 Take 2 string and display the larger string without using builtins
string1 = input('Enter the 1st string : ')
string2 = input('Enter the 2nd string : ')
count1 = 0
count2 = 0
for i in string1:
    count1 = count1 + 1
for i in string2:
    count2 = count2 + 1
if count2 > count1:
    print('larger string is',string2)
elif count1 == count2:
    print('Both strings are equal')
else:
    print('larger string is',string1)
-----------------------------------------
11. Count the number of lowercase letters in string
string = input('Enter the string : ')
count = 0
for i in string:
    if i.islower():
        count = count + 1
print('The number of lowercase letters are',count)
-------------------------------------------------
12. check wheather a string is a palimdrome or not
string = input('Enter the string : ')
if string == string[::-1]:
    print('Given string is palimdrome')
else:
    print('Given string is not palimdrome')
----------------------------------------------------
13. Find the number of lowercase and uppercase letters in pythgon string
string = input('Enter the string : ')
count_lower = 0
count_upper = 0
length = len(string)
for i in string:
    if i.islower():
        count_lower = count_lower + 1
    elif i.isupper():
        count_upper = count_upper + 1
print('The number of lowercase letters are',count_lower)
print('The number of uppercase letters are',count_upper)
---------------------------------------------------------------
14. To check if string is a Pangram or Not
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
string = input('Enter string : ')
if check(string) == True:
    print('The string is pangram')
else:
    print('The string is not pangram')
-------------------------------------------------
15. Accept a hypen seperated string and print in sorted oobder alphabatecally
print('Enter the hypen seperated string : ')
list = [n for n in input().split('-')]
list.sort()
print('-'.join(list))
------------------------------------------------------------------
16. Program to calculate the number of dogits and letters
string = input('Enter the hectrogeneous string : ')
digit = 0
letter = 0
for i in string:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        letter = letter + 1
print('The number of didgits are',digit)
print('The number of leetters are',letter)
--------------------------------------------------------------
17. Programme to form new string from first2 and last 2 char
string = input('Enter the string : ')
count = 0
for i in string:
    count = count + 1
new_string = string[0:2] + string[count-2:count]
print('The new string is',new_string)
-----------------------------------------------------------------
18. Program to count the occurances of each word in given string
string = input('Enter the string : ')
word = input('Enter the word to which find occurance : ')
a = []
count = 0
a = string.split(' ')
for i in range(0,len(a)):
    if word == a[i]:
        count = count + 1
print('Count of the word is',count)
-------------------------------------------------------
19. Python programme to check if a substring is present in a given string
string = input('Enter the string : ')
sub_string = input('Enter the sub-string : ')
if string.find(sub_string) == -1:
    print('Substring is not present')
else:
    print('Substring is present')
------------------------------------------------------------------------
20. Check wheather a string starts with specified character
string = input('Enter string : ')
start = input('Enter stat letter : ')
print(string.startswith(start))
-----------------------------------------------------------------
28. Write program for to print floating number upto 2 decimals
x = 3.14589
y = 12.99999
print("{:.3f}".format(x))
print("{:.2f}".format(y))
-------------------------------------------------------------------
29. Above programme with sign
x = 3.14589
y = -12.99999
print("{:+.3f}".format(x))
print("{:+.2f}".format(y))
------------------------------------
30. above programme with no decimal
x = 15.85896
y = -15.23967
print("{:+.0f}".format(x))
print("{:+.0f}".format(y))
--------------------------------------------
31. Programme to print the following integers with zeros on the left of specified width
33. Write a programme to display a number witha comma seperator
x = 3000000
y = 300000000
print('Number with comma seperator = '+'{:,}'.format(x))
print('Number with comma seperator = '+'{:,}'.format(y))
------------------------------------------------------------------------------
35. Programme for to count number of occurances of a substring in string
string = 'The quick brown fox jumps over the lazy dog'
print(string.count('o'))
--------------------------------------------------------------------==
36. Programme for reverse the string
string = input('Enter the string : ')
rev = ''.join(reversed(string))
print('Reverse of string is',rev)
----------------------------------------------------
37. Programme to reverse the words in a string
string = 'Prasad ganthade'
a = ' '.join(reversed(string.split()))
print(a)
----------------------------------------------------
41. Programme to print the index of the character of string
string = 'w3resorce'
for index , i in enumerate(string):
    print('character is',i,'index is',index)
------------------------------------------------------
43. Programme to convert string to list
string = 'The god colore is red and looking beautiful'
a = string.split()
print(a)
string2 = 'The-lioon-is-the-king-of-jungle'
b = string2.split('-')
print(b)
--------------------------------------------------------------
44. Programme to lowercase first n character in a string
string = 'PRASAD.GANTHADE'
print(string)
enter_num = int(input('Enter the nth character from require lowercase : '))
new_string = string[:enter_num].lower() + string[enter_num:]
print(new_string)
---------------------------------------------------------
46. Programme to count and display the vowels in given text
string = input('Enter the string : ')
def check_vowel(string,vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)

vowels = 'AaEeIiOoUu'
check_vowel(string,vowels)
------------------------------------------------------------
48 Programme to find the first non-repeating character in given string
string = 'geeksforgeeks'
index = -1
fnc = ''
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print('Either all characters are repeting or string is empty')
else:
    print('First non repeting character is',fnc)
------------------------------------------------------------------
50 Programme to find the first repeted character in a given string
string = 'geeksforgeeks'
def first_repeted_str(string):
    h = {}  # creating empty hash
    for i in string:
        if i in h:
            return i
        else:
            h[i] = 0
    return ''

print(first_repeted_str(string))
-------------------------------------------------------
52. Programme to find the first repeated word in a given string
string = 'ab cd ef ab'
def first_repeated_word(string):
    temp = set()
    for word in string.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return 'None'
print(first_repeated_word(string))
---------------------------------------------------
54 Progremme to remove spaces instring
string = input('Enter the string : ')
def remove_spaces(string):
    string = string.replace(' ','')
    return string

print(remove_spaces(string))
-----------------------------------------------
56 Programme to find the maximum occuring character in a given string
57 Program to capitalize first and last letterof each word of a given string
def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))
----------------------------------------------------------------------------------------------
58 Programme to remove duplicate characters of a given string
string = 'hello world ward'
duplicate = ''
for character in string:
    if character not in duplicate:
        duplicate = duplicate + character
print(duplicate)
-----------------------------------------------------------------
59 Program to compute sum of didgits in string
string = input('Enter the string with number : ')
def sum_digits_str(string):
    sum_digits = 0
    for i in string:
        if i.isdigit() == True:
            z = int(i)
            sum_digits = sum_digits + z

    return sum_digits
print(sum_digits_str(string))
-----------------------------
71  Programme to count uppercase, lowercase,special characterand numeric values in given string
string = input('Enter the hectrogeneous string : ')
def count_chars(string):
    upper_count, lower_count, numeric_count, special_count  = 0,0,0,0
    for i in range(0,len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            upper_count += 1
        elif string[i] >= 'a' and string[i] <= 'z':
            lower_count += 1
        elif string[i] >= '0' and string[i] <= '9':
            numeric_count += 1
        else:
            special_count += 1

    return upper_count, lower_count, numeric_count, special_count
u,l,n,s = count_chars(string)
print('Count of uppercase',u)
print('Count of lowercase',l)
print('Count of number',n)
print('Count of special',s)
--------------------------------------------------------------
75 Program to count number of non-empty substring of a given string

"""
string = 'w3resouce'





