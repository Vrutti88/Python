# Q1 WAP TO CHECK WHEATHER A NUMBER IS EVEN OR ODD
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")


# Q2 WAP TO CHECK WHEATHER THE PERSON IS ELIGIBLE FOR VOTING 
# num=int(input("Enter age:"))
# if num<18:
#     print("Cannot vote")
# else:
#     print("Can vote")


# Q3 WAP TO ENTER A NUMBER BETWEEN 1 TO 7 AS DAYS OF WEEK AND PRINT THE DAY ACCORDINGLY.(USINF IF ELIF CASE)
# num=int(input("Enter a number between 1 to 7:"))
# if num==1:
#     print("Monday")
# elif num==2:
#     print("Tuesday")
# elif num==3:
#     print("Wednesday")
# elif num==4:
#     print("Thursday")
# elif num==5:
#     print("Friday")
# elif num==6:
#     print("Saturday")
# else:
#     print("Sunday")
 


#  Q4 WAP TO ENTER A NUMBER BETWEEN 1 TO 7 AS DAYS OF WEEK AND PRINT THE DAY ACCORDINGLY.(USING MATCH CASE)
# num=int(input("Enter a number between 1 to 7:"))
# match num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")


# Q5 WAP TO CHECK WHEATHER A YEAR IS A LEAP YEAR OR NOT. 
# year=int(input("Enter a year"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,"Is a leap year")
# else:
#     print(year,"Is not a leap year")


#Q6 WAP TO CALCULATE TO TAKE IN THE MARKS OF 5 SUBJECTS, COMPUTE AVERAGE AND DISPLAY THE GRADE.
# a=int(input("Enter marks of sub_1:"))
# b=int(input("Enter marks of sub_2:"))
# c=int(input("Enter marks of sub_3:"))
# d=int(input("Enter marks of sub_4:"))
# e=int(input("Enter marks of sub_5:"))
# avg=(a+b+c+d+e)/5
# if avg>=90:
#     print("A")
# elif avg>=80:
#     print("B")
# elif avg>=70:
#     print("C")
# elif avg>=60:
#     print("D")
# else:
#     print("PASS")


#Q7 WAP TO INPUT A CHARACTER. CHECK WHETHER THE CHARACTER IS VOWEL OR CONSONANT
# char=(input("Enter a letter:"))
# if char=="a":
#     print("It is a vowel")
# elif char=="e":
#     print("It is a vowel")
# elif char=="i":
#     print("It is a vowel")
# elif char=="o":
#     print("It is a vowel")
# elif char=="u":
#     print("It is a vowel")
# else:
#     print("It is not a vowel")


#Q8 WAP TO SEARCH AN ELEMENT IN A LIST.
# def search_element(list,num):
#     for index, element in enumerate(list):
#         if element==num:
#             return index
#     return -1
# a=input("Enter a llist:")
# b=input("Enter num to be searched")
# result=search_element(a,b)
# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found in the list.")


#Q9 WAP TO TAKE A SINGLE DIGIT NUMBER FROM THE KEY BOARD AND PRINT ITS SPELLING IN ENGLISH WORD USING IF ELIF.
# num=int(input("Enter a single digit number:"))
# if num==1:
#     print("One")
# elif num==2:
#     print("Two")
# elif num==3:
#     print("Three")
# elif num==4:
#     print("Four")
# elif num==5:
#     print("Five")
# elif num==6:
#     print("Six")
# elif num==7:
#     print("Seven")
# elif num==8:
#     print("Eight")
# else:
#     print("Nine")


#Q10 WAP TO INPUT THREE NUMBERS AND ARRANGE THEM IN ASCENDING ORDER.
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# numbers=[num1,num2,num3]
# numbers.sort()
# print("The numbers in ascending order are:",numbers)


#Q11 WAP TO TAKE A SINGLE DIGIT NUMBER FROM THE KEY BOARD AND PRINT ITS SPELLING IN ENGLISH WORD USING MATCH CASE
# num=int(input("Enter a single digit number:"))
# match num:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case 6:
#         print("Six")
#     case 7:
#         print("Seven")
#     case 8:
#         print("Eight")
#     case 9:
#         print("Nine")


# Q12 WAP TO READ TWO NUMBERS AND ARITHMETIC OPERATOR PERFORM THE OPERATION AND DISPLAY THE COMPUTED RESULT.
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# operator=input("Enter an operator:")
# if operator=='+':
#     print("Answer=",num1+num2)
# elif operator=='-':
#     print("Answer=",num1-num2)
# elif operator=='*':
#     print("Answer=",num1*num2)
# elif operator=='/':
#     if num2!=0:
#         print("Answer=",num1/num2)
#     else:
#         print("Error!")
# else:
#     print("Error!! Invalid Operator.")


# Q13 WAP TO CHECK WHETHER A INPUTTED CHARACTER IS UPPERCASE OR LOWERCASE OR DIGIT OR ANY OTHER CHARACTER.
# char=input("Enter a character")
# if char.isupper():
#     print("The character is uppercase")
# elif char.islower():
#     print("The character is lowercase")
# elif char.isdigit():
#     print("The character is digit")
# else:
#     print("The character is different")


# Q14 WAP TO DEVELOP A NUMBER GUESSING GAME USING LOOPS AND CONDITIONAL STATEMENTS. ASK THE USER TO GUESS A SECRET NUMBER. IF USER HAS NOT GUESSED CORRECT NUMBER, PROVIDE HINT.
# import random
# def guessing_game():
#     secret_number=random.randint(1,100)
#     attempts=0
#     max_attempts=5
#     print("Welcome to number guessing game!!")
#     print("I have selected a number between 1 to 100.")
#     print("You have 5 attempts to guess.")
#     while attempts<max_attempts:
#         guess=input("Enter your guess:")
#         if not guess.isdigit():
#             print("Please enter a valid number")
#             continue
#         guess=int(guess)
#         attempts+=1
#         if guess==secret_number:
#             print(f"Congratulations! You've guessed the correct number: {secret_number} in {attempts} attempts.")
#             break
#         elif guess<secret_number:
#             print("Too low! Try again.")
#         else:
#             print("Too high! Try again.")
#     if attempts==max_attempts:
#         print(f"Sorry, you've used all your attempts. The secret number was: {secret_number}")
# guessing_game()


# Q15 WAP TO PROMPT USER TO ENTER NAME AND PASSWORD UNTIL IT ENTERS "stud" IN NAME AND "pass" IN PASSWORD. ALLOW ONLY 5 ATTEMPTS.
# attempts=0
# while attempts<5:
#     name=input("Enter name:")
#     pwd=input("Enter password:")
#     if name=="stud" and pwd=="pass":
#         print("Success")
#         break
#     else:
#         print("Invalid; Try again")
#         attempts+=1
# if attempts==5:
#     print("max_attempts reached")


# Q16 WAP TO DISPLAY NUMBERS FROM 15 TO 1 IN ASCENDING ORDER.
# for i in range(15,0,-1):
#     print(i,end=" ")


# Q17 WAP TO DISPLAY SUM OF NUMBERS FROM 11 TO 200 USING FOR LOOP.
# sum=0
# for i in range(11,201):
#     sum+=i
# print("sum of numbers is:",sum)


# Q18 WAP TO DISPLAY AVERAGE OF NUMBERS FROM 5 TO 15 AND 21 TO 60.
# a=range(5,16)
# b=range(21,61)
# total=sum(a)+sum(b)
# count=len(a)+len(b)
# avg=total/count
# print("Average of number is:",avg)


# Q19 WAP TO DISPLAY ODD NUMBERS FROM 5 TO 30.
# for i in range(5,30,2):
#     print(i,end=" ")


# Q20 WAP TO FIND FACTORIAL OF A NUMBER INPUTTED BYTHE USER.
# num=int(input("enter a number:"))
# if num<0:
#     print("Invalid number")
# else:
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print("factorial is",fact)


# Q21 WAP TO FIND SUM OF DIGITS OF A INT NUMBER.
# num=input("Enter an integer:")
# sum=0
# for i in num:
#     sum+=int(i)
# print("Sum of digits is:",sum)


# Q22 WAP TO DISPLAY SUM OF EVEN NUMBERS BETWEEN 30 AND 50.
# sum=0
# for i in range(30,51,2):
#     sum+=i
# print("sum is:",sum)


# Q23 WAP TO PRINT MULTIPLICATION TABLE.
# num=int(input("Enter a number for mul table:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")


# Q24 WAP TO PRINT THE FOLLOWING PATTERN.
# 1
# 22
# 333
# 4444
# for i in range(1, 5):
#     print(str(i) * i)


# Q25 WAP TO PRINT PATTERN:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,5):
#     print("*"" "*i,)
# for j in range(3,0,-1):
#     print("*" " "*j)
    

# Q26 WAP TO PRINT PATTERN:
# A  
# BB  
# CCC 
# for i in range(1, 5):
#     print(chr(64+i) * i)


# Q27 WAP TO FIND WHETHER GIVEN NUMBER IS AN ARMSTRONG NUMBER.
# def armstrong_number(num):
#     digits=str(num)
#     num_digits=len(digits)
#     armstrong_sum=sum(int(digit)**num_digits for digit in digits)
#     return armstrong_sum==num
# a=int(input("Enter a number:"))
# if armstrong_number(a):
#     print(f"{a} is an Armstrong number")
# else:
#     print(f"{a} is not an Armstrong number")


# Q28 WAP TO GENERATE THE FIBONACCI SERIES UPTO N TERMS.
# num=int(input("Enter a number:"))
# if num<0:
#     print("Invalid number")
# elif num==0:
#     print("0")
# elif num==1:
#     print("1")
# else:
#     fib_series=[]
#     fib1=0
#     fib2=1
# for i in range(num):
#     fib_series.append(fib1)
#     fib1,fib2=fib2,fib1+fib2
# print("fibonacci series", fib_series)


# Q29 WAP THAT CHECK WHETHER A NUMBER IS PRIME NUMBER OR NOT.
# num = int(input("Enter a number: "))
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# Q30 WAP TO CALCULATE SUM AND AVERAGE OF A GIVEN ARRAY : ARR=('i',[1,2,3,4,5]).
# import array
# arr=array.array('i',[1,2,3,4,5])  
# sum_array = sum(arr)
# average = sum_array / len(arr)
# print("Sum:", sum_array)
# print("Average:", average)


# Q31 WAP TO REVERSE THE ORDER OF THE ITEMS IN THE ARRAY.
# import array
# arr=array.array('i',[1,2,3,4,5]) 
# reverse=array.array('i',arr[::-1])
# print("Rversed array",reverse)


# Q32 WAP TO REMOVE DUPLICATE ELEMENTS IN A GIVEN ARRAY OF INTEGERS.
# def remove_duplicates(arr):
#     b = []
#     for num in arr:
#         if num not in b:
#             b.append(num)
#     return b
# a=input("Enter an array")
# result = remove_duplicates(a)
# print(result)

# Q33 WAP THAT TAKES A STRING AS INPUT AND PRINT IT IN REVERSE ORDER.
# a=input("Enter string:")
# reverse=a[::-1]
# print("Reversed:",reverse)


# Q34 WRITE A PROGRAM THAT COUNTS THE NUMBER OF VOWELS IN A GIVEN STRING.
# a=input("Enter a string")
# vowels="aeiouAEIOU"
# count=0
# for i in a:
#     if i in vowels:
#         count+=1
# print("Numbers of vowels",count)


# Q35 WAP THAT CHECKS IF A GIVEN STRING IS A PALINDROME.
# a=input("Enter a string:")
# b=''.join(a.split()).lower()
# if b == b[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palimdrome")


# Q36 WAP THAT REMOVES DUPLICATE CHARACTERS FROM A STRING.
# def remove_duplicates(b):
#     seen=set()
#     result=[]
#     for i in b:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return''.join(result)
# a=input("Enter a word:")
# output=remove_duplicates(a)
# print(output)


# Q37 WAP TO PRINT EVEN LENGTH WORDS IN STRING.
# a=input("Enter a string of words:")
# words=a.split()
# even= [word for word in words if len(word)%2==0]
# print("Even length words are:",even)


# Q38 WAP TO REMOVE SPACES FROM GIVEN STRING: "Python is very easy".
# n="Python is very easy"
# no_space=''.join(n.split()) 
# print(no_space)


# Q39 WAP TO CONVERT GIVEN LIST OF ASCII VALUE TO A STRING [65,66,67,68,69].
# ascii=[65, 66, 67, 68, 69]
# result=''.join(chr(value) for value in ascii)
# print("Converted string is",result)


# Q40 WAP TO PRINT THE INDIVIDUAL CHARACTERS OF THE STRING INPUTTED BY USER IN THE FOLLOWING WAY: H-e-l-l-o.
# a=input("ENter a string:")
# result='-'.join(a)
# print(result)





num=int(input("Enter a number:"))
if (num==10):
    print("You are correct!")
elif(num==9):
    print("You are wrong")
else:
     print(num,"It is even")