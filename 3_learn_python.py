# Ex. 18 Names, Variables, Code, Functions

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Cari", "Holmes")
print_two_again("Cari", "Holmes")
print_one("First!")
print_none()

# Ex. 19 Functions and Variables

# the function and what to print when it is called
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# can directly give the function the numbers needed
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# can use variables and assign them to the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# can use int and perform math with operators
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# can combine variables and int to do the math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)

# Ex. 20 Functions and Files

from sys import argv

script, input_file = argv

# the functions I will call upon later when printing
# a function to read the file
def print_all(f):
    print(f.read())

# a function to go back the beginning (0)
def rewind(f):
    f.seek(0)

# a function to count the lines
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opening my text file 
current_file = open(input_file)

print("First let's print the whole file:\n")

# printing the whole file that is being opened
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# this will take us back to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
# adding 1 to each current_line to continue counting

# seek()
# readline()