# Exercise 3.1.
# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough
# leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    total_length = 70 - len(s)
    space = " "
    total_spaces = total_length * space
    print(total_spaces + s)


word = input("Enter any word: ")
right_justify(word)

""" 
Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For example, do_twice
is a function that takes a function object as an argument and calls it twice:

def do_twice(f):
    f()
    f()
    
Here’s an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print('spam')
    
do_twice(print_spam)



"""


# 3.2.2 Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice,
# passing the value as an argument.
def do_twice(function, value):
    function(value)
    function(value)


# 3.2.3 Copy the definition of print_twice from earlier in this chapter to your script.
def print_twice(arg):
    print(arg)
    print(arg)


# 3.2.4 Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
do_twice(print_twice, 'spam')


# 3.2.5. Define a new function called do_four that takes a function object and a value and calls the function four
# times, passing the value as a parameter. There should be only two statements in the body of this function, not four. 
def do_four(function, value):
    do_twice(function, value)
    do_twice(function, value)


