# Q1) Write a Python function that accepts a string and counts the number of upper and lower count letters.
# def count(s):
#     upper_count=0
#     lower_count=0
#     for char in s:
#         if char.isupper():
#             upper_count+=1
#         elif char.islower():
#             lower_count+=1
#     return upper_count,lowercount
# string="Hello World"
# upper,lowert=count(string)
# print(f"uppercase letters are:{upper}\nlowercase letters are:{lower}")





def count_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage
string = "Hello World!"
upper, lower = count_letters(string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
