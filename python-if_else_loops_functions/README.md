Python – if / else, loops, and functions

This directory contains solutions for the python-if_else_loops_functions project in the repository
alu-higher_level_programming.

The goal of this project is not just to write working scripts, but to deeply understand core Python concepts so well that they can be explained clearly without external help.

Learning Objectives

By completing this project, I should be able to confidently explain:

General Python Concepts

Why Python is powerful and expressive

Why indentation is essential in Python (and how it defines code blocks)

How to use:

if, if ... else, and conditional logic

Comments (#) to document code

Variables and assignment

while and for loops

break and continue

else clauses on loops

pass

range()

The difference between Python’s for loop and C’s for loop

What a function is and how to define and call one

What happens when a function does not explicitly return a value

Variable scope (local vs global)

What a traceback is and how to read one

Arithmetic operators and how they work in Python

Note: Lists are not required knowledge for this project.

Requirements
Python Scripts

Allowed editors: vi, vim, emacs

Interpreted on Ubuntu 20.04 LTS

Python version: Python 3.8.5

Every file must:

Start with:

#!/usr/bin/python3

End with a new line

Be executable (chmod +x filename.py)

Follow pycodestyle (version 2.7.*)

The length of files will be tested using wc

A README.md file at the root of the project directory is mandatory.

Project Tasks
0. Positive anything is better than negative nothing

File: 0-positive_or_negative.py

Print whether a randomly generated number is:

Positive

Zero

Negative

The provided random.randint() logic must not be modified.

1. The last digit

File: 1-last_digit.py

Print:

The last digit of a random number

Whether it is:

Greater than 5

Equal to 0

Less than 6 and not 0

The line:

number = random.randint(-10000, 10000)

must not be changed.

2. Print the alphabet

File: 2-print_alphabet.py

Print the lowercase alphabet:

Using only one print

Using only one loop

Without storing characters in a variable

Without importing any module

No newline at the end

3. Print alphabet except q and e

File: 3-print_alphabt.py

Same as task 2, but:

Exclude letters q and e

4. Hexadecimal printing

File: 4-print_hexa.py

Print numbers from 0 to 98:

In decimal

In hexadecimal format (0x...)

Using only one loop and one print

5. 00...99

File: 5-print_comb2.py

Print numbers from 0 to 99:

Two digits

Separated by comma and space

Ascending order

Only one loop

At most two print statements

6. All possible combinations of two digits

File: 6-print_comb3.py

Print all combinations of two different digits:

No repeated combinations (01 is valid, 10 is not)

Ascending order

At most 2 loops

At most 3 print functions

7. islower

File: 7-islower.py

Function:

def islower(c):

Returns:

True if c is lowercase

False otherwise

Restrictions:

No imports

No str.upper() or str.isupper()

Use ord() to compare ASCII values

8. To uppercase

File: 8-uppercase.py

Function:

def uppercase(str):

Print a string in uppercase:

Only one loop

No imports

No built-in uppercase methods

Use ASCII manipulation with ord()

9. Print the last digit

File: 9-print_last_digit.py

Function:

def print_last_digit(number):

Prints the last digit

Returns the value of the last digit

10. a + b

File: 10-add.py

Function:

def add(a, b):

Return the result of a + b.

11. a ^ b

File: 11-pow.py

Function:

def pow(a, b):

Return a raised to the power of b.

12. FizzBuzz

File: 12-fizzbuzz.py

Function:

def fizzbuzz():

Print numbers from 1 to 100:

Multiples of 3 → Fizz

Multiples of 5 → Buzz

Multiples of both → FizzBuzz

Each element separated by a space

Key Concepts Practiced

This project reinforces:

Control flow

ASCII manipulation

Loop logic design

Function creation and return values

Writing clean, PEP8-compliant code

Understanding Python execution rules

It builds the mental model required to think like a Python developer rather than just writing code that “works.”

Repository Structure
alu-higher_level_programming/
└── python-if_else_loops_functions/
    ├── 0-positive_or_negative.py
    ├── 1-last_digit.py
    ├── 2-print_alphabet.py
    ├── 3-print_alphabt.py
    ├── 4-print_hexa.py
    ├── 5-print_comb2.py
    ├── 6-print_comb3.py
    ├── 7-islower.py
    ├── 8-uppercase.py
    ├── 9-print_last_digit.py
    ├── 10-add.py
    ├── 11-pow.py
    └── 12-fizzbuzz.py
Conclusion

This project establishes the foundation of structured programming in Python:

Thinking in conditions

Designing clean loops

Writing reusable functions

Respecting coding standards

Mastering these fundamentals is essential before moving to more advanced topics like lists, classes, and object-oriented programming.
