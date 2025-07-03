# Day 1 Practice - Python Basics

# 1. Greet the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + "! You are", age, "years old.")

print()  # Line break

# 2. Simple profile creator
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby: ")
print("My name is", name + ". I live in", city, "and I love", hobby + ".")

print()

# 3. Data type identification
num = 10              # int
pi = 3.14             # float
text = "Python"       # str
status = True         # bool
items = [1, 2, 3]     # list

print("Integer:", num)
print("Float:", pi)
print("String:", text)
print("Boolean:", status)
print("List:", items)

print()

# 4. Arithmetic calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient: {:.2f}".format(a / b))
print("Remainder:", a % b)
print("Power:", a ** b)

print()

# 5. Circle and rectangle calculator
radius = float(input("Enter radius of circle: "))
print("Circle Area:", 3.14 * radius ** 2)
print("Circle Circumference:", 2 * 3.14 * radius)

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
print("Rectangle Area:", length * width)
print("Rectangle Perimeter:", 2 * (length + width))

print()

# 6. Even or odd checker
num_check = int(input("Enter a number: "))
if num_check % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print()

# 7. Voting eligibility
user_age = int(input("Enter your age to check voting eligibility: "))
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print()

# 8. Grading system
user_marks = int(input("Enter your marks (0–100): "))
if user_marks < 0 or user_marks > 100:
    print("Invalid marks entered.")
elif user_marks >= 90:
    print("Grade: A")
elif user_marks >= 75:
    print("Grade: B")
elif user_marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
