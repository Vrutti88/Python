# Q1) Create a person class with:
# i) two instance variable: name, age.
# ii) Create a parameterized constructor
# Create a student class. Inherit person class in Student class.
# Student class have:
# i) instance variable: rollno and stream.
# ii) Create a parameterized constructor to initialize all instance variables of
# student class as well as Person class
# iii)Instance method: display() to print name, age, rollno and stream
# Create an object of Student class and call display method
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Student(Person):
#     def __init__(self,name,age,rollno,stream):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.stream=stream
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Roll No: {self.rollno}")
#         print(f"Stream: {self.stream}")
# student = Student("ABCD", 20, "165", "Computer Science")
# student.display()

# Q2) Write a Python class named Circle. Declare an instance variable, radius and two methods that will compute the area and the perimeter of a circle.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*(self.radius**2)
#     def perimeter(self):
#         return math.pi*2*self.radius
# radius=int(input("ENter a number:"))
# circle=Circle(radius)
# print("Area is:",circle.area())
# print("Perimeter is",circle.perimeter())


# Q3) Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         if self.b!=0:
#             return self.a/self.b
#         else:
#             return "Error:Division by zero"
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# calc=Calculator(a,b)
# print("Addition is:",calc.add())
# print("Subtraction is:",calc.sub())
# print("Multiplication is:",calc.mul())
# print("Division is:",calc.div())


# Q4) Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# class Shopping:
#     def __init__(self,):
#         self.cart={}
#     def additem(self,item_name,price,quantity=1):
#         if item_name in self.cart:
#             current_quantity=self.cart[item_name][1]
#             self.cart[item_name]=(price,current_quantity+quantity)
#         else:
#             self.cart[item_name]=(price,quantity)
#         print(f"Added {quantity} x {item_name} at ${price} each.")
#     def removeitem(self,item_name):
#         if item_name in self.cart:
#             del self.cart[item_name]
#             print(f"Removed {item_name} from the cart.")
#         else:
#             print(f"{item_name} not found in the cart.")
#     def calculate(self):
#         total = sum(price * quantity for price, quantity in self.cart.values())
#         return total
#     def show_cart(self):
#         if not self.cart:
#             print("Your cart is empty.")
#         else:
#             print("\nItems in your cart:")
#             for item, (price, quantity) in self.cart.items():
#                 print(f"{item}: ${price} x {quantity}")
#             print(f"Total Price: ${self.calculate()}\n")
# cart = Shopping()
# while True:
#     print("\nOptions:")
#     print("1. Add item to cart")
#     print("2. Remove item from cart")
#     print("3. View cart")
#     print("4. Calculate total price")
#     print("5. Exit")
#     choice = input("Choose an option (1-5): ")
#     if choice == "1":
#         item_name = input("Enter item name: ")
#         try:
#             price = float(input("Enter item price: "))
#             quantity = int(input("Enter quantity: "))
#             cart.additem(item_name, price, quantity)
#         except ValueError:
#             print("Invalid input. Please enter numeric values for price and quantity.")    
#     elif choice == "2":
#         item_name = input("Enter item name to remove: ")
#         cart.removeitem(item_name)    
#     elif choice == "3":
#         cart.show_cart()
#     elif choice == "4":
#         print(f"Total Price: ${cart.calculate()}")    
#     elif choice == "5":
#         print("Thank you for shopping!")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")


# Q5) Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# • Use 'assign_department' method to change the department of an employee.
# • Use 'print_employee_details' method to print the details of an employee
# • Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# • overtime = hours_worked - 50
#   Overtime amount = (overtime * (salary / 50))
# class Employee:
#     def __init__(self,emp_name,emp_id,emp_salary,emp_department):
#         self.emp_name=emp_name
#         self.emp_id=emp_id
#         self.emp_salary=emp_salary
#         self.emp_department=emp_department
#     def calculate_emp_salary(self,hours_worked):
#         if hours_worked>50:
#             overtime = hours_worked - 50
#             Overtime_amt = (overtime * (self.emp_salary / 50))
#             total_sal=self.emp_salary+Overtime_amt
#         else:
#             total_sal=self.emp_salary
#         return total_sal
#     def emp_assign_department(self,new_department):
#         self.emp_department = new_department    
#         print(f"{self.emp_name}'s department is assigned to {self.emp_department}")
#     def print_employee_details(self):
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Employee name: {self.emp_name}")
#         print(f"Employee salary: ${self.emp_salary}")
#         print(f"Employee department: {self.emp_department}")
# emp1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
# emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
# emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
# emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# emp1.print_employee_details()
# print("\n")

# emp2.emp_assign_department("MARKETING")
# emp2.print_employee_details()
# print("\n")

# hours_worked = 55
# print(f"{emp3.emp_name}'s salary with {hours_worked} hours worked: ${emp3.calculate_emp_salary(hours_worked):.2f}")
# print("\n")

# emp4.print_employee_details()
# print("\n")


# Q6) Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
# class BankAccount:
#     def __init__(self, account_number, balance, date_of_opening, customer_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.date_of_opening = date_of_opening
#         self.customer_name = customer_name

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount} has been deposited. New balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance.")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive.")
#         else:
#             self.balance -= amount
#             print(f"${amount} has been withdrawn. New balance: ${self.balance}")

#     def check_balance(self):
#         print(f"The current balance for account {self.account_number} is ${self.balance}")

# account_number = input("Enter account number: ")
# customer_name = input("Enter your name: ")
# date_of_opening = input("Enter the date of opening (YYYY-MM-DD): ")
# balance = float(input("Enter balance: "))
# deposit_amount = float(input("Enter amount to deposit: "))
# withdraw_amount = float(input("Enter amount to withdraw: "))

# account1 = BankAccount(account_number, balance, date_of_opening, customer_name)

# account1.deposit(deposit_amount)
# account1.withdraw(withdraw_amount)

# account1.check_balance()


# Q7) Create a class hierarchy for different types of geometric shapes, including circles, rectangles, and triangles, using inheritance.
# Tasks:
# A. Define a base class called Shape with common attributes like colour and area.
# B. Implement subclasses for specific shape types such as Circle, Rectangle, and Triangle. Each subclass should inherit from the Shape class.
# C. Incorporate additional attributes and methods specific to each shape type. For example, a Circle class might have attributes like radius and methods like calculate_area.
# D. Use inheritance to create subclasses representing variations within each shape type. For example, within the Rectangle class, create subclasses for Square and Parallelogram.
# E. Implement methods or attributes in the subclasses to demonstrate how inheritance allows for the sharing of attributes and methods from parent classes.
# F. Create instances of the various shape classes and test their functionality to ensure that attributes and methods work as expected.
# import math
# class Shape:
#     def __init__(self,colour,):
#         self.colour=colour
#     def area(self):
#         raise NotImplementedError("Subclasses should implement this method")
#     def __str__(self):
#         return f"A {self.colour} shape" 
# class Circle(Shape):
#     def __init__(self,radius,colour):
#         super().__init__(colour)
#         self.radius=radius
#     def area(self):
#         return math.pi*(self.radius**2)
#     def __str__(self):
#         return f"{super().__str__()} - Circle with radius {self.radius}"
# class Rectangle(Shape):
#     def __init__(self,length,breadth,colour):
#         super().__init__(colour)
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
#     def __str__(self):
#         return f"{super().__str__()} - Rectangle with length {self.length} and breadth {self.breadth}"
# class Triangle(Shape):
#     def __init__(self,base,height,colour):
#         super().__init__(colour)
#         self.base=base
#         self.height=height
#     def area(self):
#         return 0.5*self.base*self.height
#     def __str__(self):
#         return f"{super().__str__()} - Triangle with base {self.base} and height {self.height}"
# cir_rad=int(input("Enter radius of circle: "))
# cir_col=input("Enter colour for circle: ")
# rect_len=int(input("Enter length of rectangle: "))
# rect_bred=int(input("Enter breadth of rectangle: "))
# rect_col=input("Enter colour for rectangle: ")
# tri_base=int(input("Enter base of triangle: "))
# tri_hei=int(input("Enter height of triangle: "))
# tri_col=input("Enter colour for triangle: ")
# if __name__=="__main__":
#     circle=Circle(cir_rad,cir_col)
#     rectangle=Rectangle(rect_len,rect_bred,rect_col)
#     triangle=Triangle(tri_base,tri_hei,tri_col)
#     shapes=[circle,rectangle,triangle]
#     for shape in shapes:
#         print(shape)
#         print(f"Area: {shape.area():.2f}\n")


# Q8) WAP to find the number of words in the given text file [Hints: Use the split() method to separate words.]
# def count(file):
#     with open(file, 'r') as f:  
#         text = f.read()  
#         words = text.split()  
#         num_words = len(words)  
#         return num_words   
# file_path = input("Enter the path to the text file: ")
# word_count = count(file_path)  
# print(f"The number of words in the file is: {word_count}")


# Q9) Write a program to write “Happy Programming” in a text file and read it
# file_name="file.txt"
# with open(file_name,'w') as f:
#     f.write("Happy Programming")
# with open(file_name,'r') as f:
#     content=f.read()
#     print(content)


# Q10) WAP to demonstrate the working of the following functions:
# i) read()
# ii) read(n)
# iii)readline()
# iv) readlines()
# with open("file.txt",'w') as f:
#     f.write("Line1: Hello World\n")
#     f.write("Line2: My name is Python\n")
#     f.write("Line3: Welcome to programming\n")
#     f.write("Line4: Start code")
# print("\nread()")
# with open("file.txt",'r') as f:
#     content=f.read()
#     print(content)
# print("\nread(n)")
# with open("file.txt",'r') as f:
#     char=f.read(13)
#     print(char)
# print("\nreadline()")
# with open ("file.txt",'r') as f:
#     line=f.readline()
#     print(line.strip())
# print("\nreadlines()")
# with open ("file.txt",'r') as f:
#     lines=f.readlines()
#     for lin in lines:
#         print(lin.strip())


# Q11) WAP that exhibits the working of the following functions:
# i. write()
# ii. writelines()
# with open("file.txt",'w') as f:
#     f.write("Line1: Hello World\n")
#     f.write("Line2: My name is Python\n")
# print("write()")
# with open("file.txt",'r') as f:
#     content=f.read()
#     print(content)
# lines=[
#     "This is the first line\n",
#     "This is the second line\n",
#     "This is the third line\n",
#     "This is the fourth line\n"
# ]
# with open("file.txt",'a') as f:
#     f.writelines(lines)
# print("writelines()")
# with open("file.txt",'r') as f:
#     content=f.read()
#     print(content)


# Q12) Write a Python program to read first n lines of a file.
# file_name = "file.txt"
# def read(file_name,n):
#     with open(file_name,'r') as f:
#         for i in range(n):
#             line=f.readline()  
#             if line == '': 
#                 break
#             print(line.strip())  
# n=int(input("Enter the number: "))
# read(file_name,n)


# Q13) Write a Python program to append text to a file and display the text.
# with open("file.txt",'w') as f:
#     f.write("Line1: Hello World\n")
#     f.write("Line2: My name is Python\n")
# with open("file.txt",'r') as f:
#     print(f.read())
# lines=[
#     "This is the first line\n",
#     "This is the second line\n",
#     "This is the third line\n",
#     "This is the fourth line\n"
# ]
# with open("file.txt",'a') as f:
#     f.writelines(lines)
# with open("file.txt",'r') as f:
#     print(f.read())


# Q14) Write a Python program to read last n lines of a file.
# from collections import deque
# file_name = "file.txt"
# def read(file_name,n):
#     with open(file_name,'r') as f:
#         last_lines = deque(f, maxlen=n)
#         for line in last_lines:
#             print(line.strip())  
# n=int(input("Enter the number: "))
# read(file_name,n)


# Q15) Write a Python program to read a file line by line and store it into a list.
# lines=[]
# with open("file.txt",'r') as f:
#     for line in f:
#        lines.append(line.strip())
# print(lines)

# Q16) Write a program to exhibit these concepts:
# i. try
# ii. except
# iii. finally
# try:
#     num=int(input("Enetr numerator: "))
#     den=int(input("Enetr denominator: "))
#     result=num/den
#     print(f"The result is {result}")
# except ZeroDivisionError:
#         print("Error:Cannot divide by zero")
# except ValueError:
#     print("Error:Enter a valid number")
# finally:
#     print("Execution is completed")


# Q17) Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
# try:
#     num=int(input("Enetr numerator: "))
#     den=int(input("Enetr denominator: "))
#     result=num/den
#     print(f"The result is {result}")
# except ZeroDivisionError:
#         print("Error:Cannot divide by zero")
# except ValueError:
#     print("Error:Enter a valid number")


# Q18) Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# try:
#     a=int(input("Enter an integer: "))
#     print(a)
# except ValueError:
#     print("Error:Enter a valid number")


# Q19) WAP that exhibits multiple except blocks along with default block
# try:
#     num=int(input("Enetr numerator: "))
#     den=int(input("Enetr denominator: "))
#     result=num/den
#     print(f"The result is {result}")
# except ZeroDivisionError:
#         print("Error:Cannot divide by zero")
# except ValueError:
#     print("Error:Enter a valid number")
# except TypeError:
#     print("Error:Invalid input")
# except Exception as e:
#     peinr(f"Error: {e}")


# Q20) WAP that exhibits except blocks that can catch multiple exceptions.
# try:
#     num=int(input("Enetr numerator: "))
#     den=int(input("Enetr denominator: "))
#     result=num/den
#     print(f"The result is {result}")
# except (ZeroDivisionError,ValueError) as e:
#     print(f"Error: {e}")


# Q21) WAP to demonstrate how to use lambda in map() function.
# numbers=[1,2,3,4]
# square=list(map(lambda x : x**2,numbers))
# print(f"Original: {numbers}")
# print(f"Squared: {square}")


# Q22) WAP to demonstrate how to use lambda in filter() function.
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x : x%2==0,numbers))
# print(f"Original: {numbers}")
# print(f"Even numbers: {even}")


# # Q23) Write a Python program to filter a list of integers into list of even numbers and list of odd numbers using Lambda. [Hint: use lambda in filter() ]]
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x : x%2==0,numbers))
# odd=list(filter(lambda x : x%2!=0,numbers))
# print(f"Original: {numbers}")
# print(f"Even numbers: {even}")
# print(f"Odd numbers: {odd}")


# Q24) Write a Python program to square and cube every number in a given list of integers using Lambda. [Hint: use lambda in map()].
# numbers=[1,2,3,4,5,6,7,8,9,10]
# square=list(map(lambda x : x**2,numbers))
# cube=list(map(lambda x : x**3,numbers))
# print(f"Original: {numbers}")
# print(f"Square: {square}")
# print(f"Cube numbers: {cube}")


# Q25) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument.
# num=int(input("Enetr a number: "))
# add=lambda x:x+15
# result=add(num)
# print(f"The result is: {result}")


# Q26) Create a lambda function that multiplies argument x with argument y and prints the result.
# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# mul=lambda x,y:x*y
# result=mul(x,y)
# print(f"The result is: {result}")