# Project 1: Student Management Project
# Create a menu based Python application for maintaining student information (rollno, name, marks). It contains basic functions which include:
# i. Add student information
# ii. display student information,
# iii. search student using rollno
# iv. remove the student.
# v. display total number of students records
# students = []
# def add_student():
#     rollno = input("Enter Roll Number: ")
#     name = input("Enter Name: ")
#     marks = float(input("Enter Marks: "))
#     students.append({'rollno': rollno, 'name': name, 'marks': marks})
#     print(f"Student {name} added successfully!\n")
# def display_students():
#     if not students:
#         print("No student records available.\n")
#         return
#     print("Student Records:")
#     print("Roll No\tName\tMarks")
#     print("-------------------------")
#     for student in students:
#         print(f"{student['rollno']}\t{student['name']}\t{student['marks']}")
#     print()
# def search_student():
#     rollno = input("Enter Roll Number to search: ")
#     for student in students:
#         if student['rollno'] == rollno:
#             print("Student Found:")
#             print(f"Roll No: {student['rollno']}, Name: {student['name']}, Marks: {student['marks']}\n")
#             return
#     print("Student not found.\n")
# def remove_student():
#     rollno = input("Enter Roll Number to remove: ")
#     for student in students:
#         if student['rollno'] == rollno:
#             students.remove(student)
#             print(f"Student with Roll No {rollno} removed successfully!\n")
#             return
#     print("Student not found.\n")
# def total_students():
#     print(f"Total number of student records: {len(students)}\n")
# def menu():
#     while True:
#         print("Student Management System")
#         print("1. Add Student")
#         print("2. Display Students")
#         print("3. Search Student by Roll No")
#         print("4. Remove Student")
#         print("5. Display Total Number of Students")
#         print("6. Exit")
#         choice = input("Enter your choice (1-6): ")
#         if choice == '1':
#             add_student()
#         elif choice == '2':
#             display_students()
#         elif choice == '3':
#             search_student()
#         elif choice == '4':
#             remove_student()
#         elif choice == '5':
#             total_students()
#         elif choice == '6':
#             print("Exiting the Student Management System. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")
# menu()


# Project 2: ATM Simulator project
# Create a simple console based ATM Simulator system. It contains various functions which include Withdrawing amount, Depositing amount and changing the pin. Here, at first the user has to enter an existing username, when the username matches the system proceed toward the next procedure i.e asking pin number. When a user passes all these sign-in procedures, he/she can use all those features.
# Features:
# 1. Sign In
# 2. Withdraw amount
# 3. Deposit amount
# 4. Change Pin
# ATM Simulator
# users = {
#     "user1": {"pin": "1234", "balance": 1000},
#     "user2": {"pin": "5678", "balance": 2000},
# }
# def sign_in():
#     username = input("Enter Username: ")
#     if username in users:
#         for _ in range(3): 
#             pin = input("Enter PIN: ")
#             if pin == users[username]["pin"]:
#                 print(f"Welcome, {username}!\n")
#                 return username
#             else:
#                 print("Incorrect PIN. Try again.")
#         print("Too many incorrect attempts. Exiting.\n")
#         return None
#     else:
#         print("Username not found.\n")
# def withdraw_amount(username):
#     amount = float(input("Enter amount to withdraw: "))
#     if amount <= users[username]["balance"]:
#         users[username]["balance"] -= amount
#         print(f"Withdrawal successful! New balance: ${users[username]['balance']:.2f}\n")
#     else:
#         print("Insufficient balance.\n")
# def deposit_amount(username):
#     amount = float(input("Enter amount to deposit: "))
#     users[username]["balance"] += amount
#     print(f"Deposit successful! New balance: ${users[username]['balance']:.2f}\n")
# def change_pin(username):
#     current_pin = input("Enter current PIN: ")
#     if current_pin == users[username]["pin"]:
#         new_pin = input("Enter new PIN: ")
#         confirm_pin = input("Confirm new PIN: ")
#         if new_pin == confirm_pin:
#             users[username]["pin"] = new_pin
#             print("PIN changed successfully!\n")
#         else:
#             print("PIN confirmation does not match.\n")
#     else:
#         print("Incorrect current PIN.\n")
# def atm_menu(username):
#     while True:
#         print("ATM Menu:")
#         print("1. Withdraw Amount")
#         print("2. Deposit Amount")
#         print("3. Change PIN")
#         print("4. Logout")
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == '1':
#             withdraw_amount(username)
#         elif choice == '2':
#             deposit_amount(username)
#         elif choice == '3':
#             change_pin(username)
#         elif choice == '4':
#             print("Logging out. Thank you for using our ATM!\n")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")
# def main():
#     print("Welcome to the ATM Simulator")
#     username = sign_in()
#     if username:
#         atm_menu(username)
# main()


# Project 3: Simple GUI calculator using Tkinter
# import tkinter as tk
# from tkinter import messagebox
# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, current + str(number))
# def clear():
#     entry.delete(0, tk.END)
# def evaluate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except Exception as e:
#         messagebox.showerror("Error", "Invalid Input")
# root = tk.Tk()
# root.title("Simple Calculator")
# entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 16), justify='right')
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# button_values = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]
# for text, row, col in button_values:
#     if text == "=":
#         button = tk.Button(root, text=text, padx=20, pady=20, bg="lightgreen", font=('Arial', 14),
#                            command=evaluate)
#     elif text == "C":
#         button = tk.Button(root, text=text, padx=20, pady=20, bg="lightcoral", font=('Arial', 14),
#                            command=clear)
#     else:
#         button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
#                            command=lambda t=text: button_click(t))
#     button.grid(row=row, column=col, sticky="nsew")
# for i in range(5):  
#     root.grid_rowconfigure(i, weight=1)
# for i in range(4): 
#     root.grid_columnconfigure(i, weight=1)
# root.mainloop()


# Project 4: Digital Clock
# Create a digital clock GUI application with Python.
# import tkinter as tk
# from time import strftime
# def update_time():
#     current_time = strftime("%H:%M:%S %p") 
#     label.config(text=current_time)  
# root = tk.Tk()
# root.title("Digital Clock")
# root.configure(bg="black")
# label = tk.Label(
#     root,
#     font=("Helvetica", 48, "bold"),
#     background="black",
#     foreground="cyan"
# )
# label.pack(anchor="center", pady=50)
# update_time()
# root.mainloop()


# Project 5: Simple Interest Calculator
# Create Simple Interest Calculator GUI application with Python.
# import tkinter as tk
# from tkinter import messagebox
# def calculate_interest():
#     try:
#         principal = float(principal_entry.get())
#         rate = float(rate_entry.get())
#         time = float(time_entry.get())
#         simple_interest = (principal * rate * time) / 100
#         result_label.config(text=f"Simple Interest: ₹{simple_interest:.2f}")
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
# def clear_fields():
#     principal_entry.delete(0, tk.END)
#     rate_entry.delete(0, tk.END)
#     time_entry.delete(0, tk.END)
#     result_label.config(text="")

# root = tk.Tk()
# root.title("Simple Interest Calculator")
# root.geometry("400x300")
# root.configure(bg="lightblue")

# title_label = tk.Label(root, text="Simple Interest Calculator", font=("Helvetica", 18, "bold"), bg="lightblue")
# title_label.pack(pady=10)

# frame = tk.Frame(root, bg="lightblue")
# frame.pack(pady=10)

# principal_label = tk.Label(frame, text="Principal (₹):", font=("Helvetica", 14), bg="lightblue")
# principal_label.grid(row=0, column=0, pady=5, sticky="w")
# principal_entry = tk.Entry(frame, width=20, font=("Helvetica", 14))
# principal_entry.grid(row=0, column=1, pady=5)

# rate_label = tk.Label(frame, text="Rate of Interest (%):", font=("Helvetica", 14), bg="lightblue")
# rate_label.grid(row=1, column=0, pady=5, sticky="w")
# rate_entry = tk.Entry(frame, width=20, font=("Helvetica", 14))
# rate_entry.grid(row=1, column=1, pady=5)

# time_label = tk.Label(frame, text="Time (years):", font=("Helvetica", 14), bg="lightblue")
# time_label.grid(row=2, column=0, pady=5, sticky="w")
# time_entry = tk.Entry(frame, width=20, font=("Helvetica", 14))
# time_entry.grid(row=2, column=1, pady=5)

# button_frame = tk.Frame(root, bg="lightblue")
# button_frame.pack(pady=10)

# calculate_button = tk.Button(button_frame, text="Calculate", font=("Helvetica", 14), command=calculate_interest, bg="green", fg="white")
# calculate_button.grid(row=0, column=0, padx=10)

# clear_button = tk.Button(button_frame, text="Clear", font=("Helvetica", 14), command=clear_fields, bg="red", fg="white")
# clear_button.grid(row=0, column=1, padx=10)

# result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="lightblue")
# result_label.pack(pady=10)
# root.mainloop()