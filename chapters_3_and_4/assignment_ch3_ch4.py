"""
Python Fundamentals - Chapters 3 & 4
Coursework from Automate the Boring Stuff with Python, 3rd Edition.

Covers loops (while/for, range, break/continue, modules) and user-defined
functions (parameters, return values, scope, try/except).
"""


# ============================================================
# SECTION A: CHAPTER 3 - LOOPS
# ============================================================


# ------------------------------------------------------------
# Part A1: Short Answer
# ------------------------------------------------------------

# A1.1  Difference between a while loop and a for loop.
a1_1_answer = "while loops through as long as a condition is true, and for runs for a certain number of iterations"

# A1.2  What break and continue do.
a1_2_answer = "break stops the program and continue passes through"

# A1.3  What an infinite loop is, and how to stop one.
a1_3_answer = "infinite loop keeps running because there is nothing to stop it. control c stops it"

# A1.4  What a module is, with one example.
a1_4_answer = "a file with code that can be used/imported into other files. example is random which helps generate random numbers"


# ------------------------------------------------------------
# Part A2: Predict the Output
# ------------------------------------------------------------

# A2.1  for i in range(5): print(i)
a2_1_prediction = "0 1 2 3 4"

# A2.2  for i in range(2, 8): print(i)
a2_2_prediction = "2 3 4 5 6 7"

# A2.3  for i in range(0, 20, 4): print(i)
a2_3_prediction = "0 4 8 12 16"

# A2.4  for i in range(10, 0, -2): print(i)
a2_4_prediction = "10 8 6 4 2"

# A2.5  x = 0; while x < 10: x = x + 3
a2_5_iterations = 4
a2_5_final_x = 12

# A2.6  Same as A2.1 but break when i == 3.
a2_6_prediction = "0 1 2"

# A2.7  Same as A2.1 but continue when i == 3.
a2_7_prediction = "0 1 2 4"


# ------------------------------------------------------------
# Part A3: Fix the Bug
# ------------------------------------------------------------

# A3.1  Print 1 through 5 (was stopping at 4 because count < 5).
count = 1
while count <= 5:
    print(count)
    count = count + 1


# A3.2  Print 10 down to 1 (was infinite because n was being incremented).
n = 10
while n > 0:
    print(n)
    n = n - 1


# A3.3  Print every even number from 0 to 20 (was stopping at 18).
for i in range(0, 21):
    if i % 2 == 0:
        print(i)


# ------------------------------------------------------------
# Part A4: Write Loops From Scratch
# ------------------------------------------------------------

# A4.1  Multiplication table for 7 from 7*1 through 7*12.
for i in range(1, 13):
    print(f"7 x {i} = {7 * i}")


# A4.2  Sum of integers 1 to 100 with a while loop (Gauss problem -> 5050).
total = 0
i = 1
while i <= 100:
    total = total + i
    i = i + 1
print(total)


# A4.3  Keep asking until the user enters a number 0 < n < 100.
number = int(input())
while True:
    if number > 0 and number < 100:
        print(f"Got it: {number}")
        break


# ============================================================
# SECTION B: CHAPTER 4 - FUNCTIONS
# ============================================================


# ------------------------------------------------------------
# Part B1: Short Answer
# ------------------------------------------------------------

# B1.1  Difference between a PARAMETER and an ARGUMENT.
b1_1_answer = "parameter: variable used in function definition | argument: value passed into the function variable"

# B1.2  Difference between PRINTING and RETURNING a value.
b1_2_answer = "printing prints it out on screen, return just sends the value for future use"

# B1.3  What a function returns if it has no return statement.
b1_3_answer = "none"

# B1.4  Difference between LOCAL and GLOBAL variables.
b1_4_answer = "local: only in function | global: entire file"

# B1.5  What the global statement is used for, with a tiny example.
b1_5_answer = "makes a value global so it can be accessed/changed anywhere"
# ex: global x; x = 10


# ------------------------------------------------------------
# Part B2: Predict the Output
# ------------------------------------------------------------

# B2.1  def greet(name): print('Hello, ' + name); result = greet('Ellie'); print(result)
b2_1_prediction = "Hello, Ellie"

# B2.2  def double(x): return x * 2; double(double(5))
b2_2_prediction = "20"

# B2.3  def add(a, b=10): return a + b
b2_3_prediction = "15 25 101"

# B2.4  Local x = 10 inside function does not change outer x = 5.
b2_4_prediction = "5"

# B2.5  Same as B2.4 but with `global x` -> outer x becomes 10.
b2_5_prediction = "10"


# ------------------------------------------------------------
# Part B3: Fix the Bug
# ------------------------------------------------------------

# B3.1  The function printed the square but didn't return it, so result was None.
def square(n):
    return n * n


result = square(5)
print(f"The square is: {result}")


# B3.2  The original call passed only one argument when two were required.
def greet(name, greeting):
    print(greeting + ", " + name + "!")


greet("Ellie", "Hello")


# ------------------------------------------------------------
# Part B4: Write Functions From Scratch
# ------------------------------------------------------------

# B4.1  Count down from `start` to 1, then print 'Blast off!'.
def countdown(start):
    while start >= 0:
        if start > 0:
            print(start)
        else:
            print("Blast off!")
        start = start - 1


countdown(5)


# B4.2  Return True if n is even, False otherwise. Use it to print evens 1-20.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


for i in range(1, 21):
    if is_even(i):
        print(i)


# B4.3  Return the sum of integers from 1 to n inclusive.
def sum_to(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result


print(sum_to(5))


# B4.4  Divide two numbers, gracefully handling division by zero.
def safe_divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Cannot divide by zero!")
        return None


print(safe_divide(10, 0))


# B4.5  Return how many digits the binary representation of n has.
def count_binary_digits(n):
    if n <= 0:
        print("Please provide a positive integer.")
        return None
    else:
        return len(bin(n)) - 2


print(count_binary_digits(5))
for i in range(1, 17):
    print(count_binary_digits(i))