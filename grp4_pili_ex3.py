#Exercise #3
#A program for you calculate the length of a string.
string = "Romblon James"
length = len(string)
print("Length of the string is", length)
print()

# A program count the number of characters in a string.
string="Dianca Mae"
char_count=len(string)
print("Number of characters in the string is", char_count)
print()

#A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
string = "lolobron"
first_char= string[0]
modified_string=first_char + string[1:].replace(first_char, '$')
print("Modified string:", modified_string)
print()

# A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = "Travis"
str2 = "Cat"

new_str1=str2[:2] + str1[2:]
new_str2=str1[:2] + str2[2:]

res= new_str1 + " " + new_str2
print("Resulting string:", res)
print()

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
var1= "Bumalik"
var2= "ka"
var3= "na"
var4= "sakin"
res= var1 + " " + var2 + " " + var3 + " " + var4
print("Concatenated string-",res)
print()

# Using + Concatenate Strings in Python get two strings from user input and concatenate them
str1= "Lebron"
str2= "James"

res=str1 + " " + str2
print("Concatenated string-", res)
print()


# Using + Concatenate in Python using your name and your age in a paragraph
name="Pili, Jayson"
age=18
result="I'm " + name + ", I'm " + str(age) + " years old"
print(result)