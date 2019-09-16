# Ex. 13 Parameters, Unpacking, Variables

# In terminal, cd into correct folder and then run the script from there.
from sys import argv
# script is the title of the document working out of
script, first, second, third = argv

print("the script is called: ", script)
print("the first is called: ", first)
print("the second is called: ", second)
print("the third is called: ", third)

# how is looked in the terminal
# Caris-MBP:Codeup cari$ python 3_learn_python.py apple banana mango
# the script is called:  3_learn_python.py
# the first is called:  apple
# the second is called:  banana
# the third is called:  mango


# Ex. 14 Prompting and Passing

from sys import argv

script, user_name = argv
# This is where the user will answer
prompt = '>'
# using f-string to fill in {}
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# Ex. 15 Reading Files

# importing from the system module
from sys import argv

script, filename = argv
# use 'open' to open the filename
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())

# using input to prompt the user to open the text file again.
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
# .read() allows you to read a file

# Ex. 16 Reading and Writing Files

from sys import argv

script, filename = argv
# formatted the sting 
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# prompted for unput after printing stings out.
input("?")

print("Opening the file...")
# opened a new txt file
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# lines to put into the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# closing the file I just made
target.close()

# Ex. 17 More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv
# copied on file to another
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
# closed the files with '.close()
out_file.close()
in_file.close()
