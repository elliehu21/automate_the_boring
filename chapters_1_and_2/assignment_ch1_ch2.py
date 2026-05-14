"""
Python Fundamentals - Chapters 1 & 2
Coursework from Automate the Boring Stuff with Python, 3rd Edition.

Covers Python basics (expressions, data types, operators, binary, logical
operators) and conditional flow (comparison operators, if/elif/else).
"""


# ============================================================
# SECTION A: CHAPTER 1 - PYTHON BASICS
# ============================================================


# ------------------------------------------------------------
# Part A1: Short Answer
# ------------------------------------------------------------

# A1.1  Difference between an EXPRESSION and a STATEMENT.
a1_1_answer = "Expressions are lines that can be evaluated to get a value. Statements are commands that do an action."

# A1.2  Three numeric data types from Chapter 1, with example values.
a1_2_answer = "Float: 1.0 | Integer: 2 | Double: 3.456"

# A1.3  What // does, and how it differs from /.
a1_3_answer = "// performs integer division (returns the quotient without the remainder), while / performs floating-point division (returns a float result)"

# A1.4  Rules for a valid Python variable name.
a1_4_answer = "1. Can't be the name of a built in python statement 2. Can't start with a number 3. Can be made up of letters, numbers, and underscores"


# ------------------------------------------------------------
# Part A2: Predict the Output
# ------------------------------------------------------------

# A2.1  'Hello' + ' ' + 'Ellie'
a2_1_prediction = "Hello Ellie"

# A2.2  'Na' * 4
a2_2_prediction = "NaNaNaNa"

# A2.3  17 % 5
a2_3_prediction = 2

# A2.4  2 ** 10
a2_4_prediction = 1024

# A2.5  Type of 10 / 2
a2_5_prediction = "float"

# A2.6  Why 'I am ' + 17 + ' years old' errors.
a2_6_explanation = "17 is an integer so cannot be concatenated with the strings"

# A2.7  Rewrite so it produces 'I am 17 years old'.
a2_7_fixed = 'I am ' + str(17) + ' years old'


# ------------------------------------------------------------
# Part A3: Binary
# ------------------------------------------------------------

# A3.1  Convert binary 1011 to decimal.
# Work: 1 + 2 + 0 + 8 = 11
a3_1_answer = 11

# A3.2  Convert decimal 25 to binary.
# Work: 16 + 8 + 1 = 2^4 + 2^3 + 2^0 -> 11001
a3_2_answer = "0001 1001"

# A3.3  Largest unsigned integer representable in 8 bits.
a3_3_answer = 255
a3_3_explanation = "The largest number would correspond to 11111111 in binary. This means 1+2^1+2^2+2^3+2^4+2^5+2^6+2^7=255"
# Number of distinct values 8 bits can represent.
a3_3_spaces = 256

# A3.4  Print the binary representation of 42 using bin().
print(bin(42))


# ------------------------------------------------------------
# Part A4: Logical Operators
# ------------------------------------------------------------

# A4.1  The three logical operators in Python.
a4_1_answer = "and, or, not"

# A4.2  Predict the value of each expression.
a4_2a = True       # True and True
a4_2b = False      # True and False
a4_2c = True       # False or True
a4_2d = False      # False or False
a4_2e = False      # not True
a4_2f = True       # not (True and False)
a4_2g = True       # (True and False) or (not False)

# A4.3  Short-circuit evaluation, with an example.
a4_3_answer = "Stopped once a result is determined. ex: True or False, once you know it's True you can stop"


# ============================================================
# SECTION B: CHAPTER 2 - IF-ELSE AND FLOW CONTROL
# ============================================================


# ------------------------------------------------------------
# Part B1: Comparison Operators
# ------------------------------------------------------------

# B1.1  The six comparison operators and their meanings.
b1_1_answer = ">: greater than, <: less than, ==: equals to, !=: not equals to, >=: greater or equal to, <=: less than or equal to"

# B1.2  Predict the value of each expression.
b1_2a = True       # 10 == 10
b1_2b = False      # 10 == '10'
b1_2c = False      # 10 != 10.0
b1_2d = True       # 'cat' < 'dog'
b1_2e = True       # 5 >= 5 and 5 <= 5
b1_2f = True       # (3 > 2) or (2 > 3)
b1_2g = False      # not (10 == 10)


# ------------------------------------------------------------
# Part B2: Reading if/elif/else
# ------------------------------------------------------------

# B2.1  Predict the printed output of:
#   if x < 0: print('A')
#   elif x == 0: print('B')
#   elif x < 10: print('C')
#   else: print('D')
b2_1a_prediction = "A"   # x = -5
b2_1b_prediction = "B"   # x = 0
b2_1c_prediction = "C"   # x = 5
b2_1d_prediction = "D"   # x = 100

# B2.2  Why does an if/elif/else chain stop checking after a True branch?
b2_2_answer = "No. This is useful because the processor won't have to run through extra code"


# ------------------------------------------------------------
# Part B3: Fix the Buggy Code
# ------------------------------------------------------------

# B3.1  Print 'Positive' / 'Negative' / 'Zero' based on the value of number.
number = 5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# B3.2  Print 'Access granted' only if BOTH username and password match.
username = 'ellie'
password = 'wrongpassword'
if username == 'ellie' and password == 'python123':
    print("Access granted")
else:
    print("Access denied")


# ------------------------------------------------------------
# Part B4: Write Code from Scratch
# ------------------------------------------------------------

# B4.1  Binary bit checker - classify a 4-character bit string.
bit_string = "1011"
if bit_string == "0000":
    print("All bits off")
elif bit_string == "1111":
    print("All bits on")
elif bit_string.startswith("1") and bit_string.endswith("1"):
    print("Endpoints on")
else:
    print("Mixed pattern")

# B4.2  Leap year checker - applies the full Gregorian rule.
year = 2100
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# B4.3  Number categorizer - prints every applicable label.
n = 2
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
if n % 10 == 0 and n != 0:
    print("Multiple of 10")
if bin(n).count("1") == 1 and n > 0:
    print("Power of 2")