# Ex. 1 A Good First Program

print("Hello world!")
print("hello again")
print("i like typing this")
print("This is fun")
print("Yay! Print!")
print("i'd much rather you 'not'")
print('I "said" do not touch this.')
# This is an example of the print feature.

# Ex. 2 Comments and Pound Characters
print("I could have run code like this.") # and the comment after is ignore.
# You can also use a comment to "disable" or comment out code:
# print("This won't run.")

print("This will run.")

# Ex. 3 Numbers and Math
+ plus
- minus
/ slash
* asterisk
% percent
< less than
> greater than
<= less than or equal to
>= greater than or equal to 

# These are examples of using math  operators
print("I will now count my chickens:")
print("hens", 25 + 30 / 6)
print("roosters:", 100 - 25 * 3 % 4)

print("I will now count the eggs:")
print(3+ 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3+2<5-7?")

print(3+2<5-7)

print("What is 3+2?", 3+2)
print("What is 5-7?", 5-7)

print("Oh, that's why it's false.")

print("How about some more?")

print("Is it greater?", 5>-2)
print("Is it greater or equal?", 5>=-2)
print("Is it less or equal?", 5<=-2)

# Ex 4. Variables and Names

# This is an example of creating variable names
cars = 100
space_in_cars = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars

average_passenger_per_car = passengers / cars_driven
# This example uses the variable names with strings in the print statements.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")

# Ex. 5 More Variables and Printing

name = 'Cari Holmes'
age = 29 # not a lie
height = 67 # inches
weight = 120 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'brown'

# Using the f" to format the strings and print.
print(f"Let's talk about {name}.")
print(f"She's {height}  inches tall.")
print(f"She's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Ex. 6 Strings and Text

types_of_people = 10
# using f-string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# using f-string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
#printing an f-string
print(f"I said: {x}")
print(f"I also said: '{y}' ")

# using .format on an already created string to add in the formatting
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."
print (w + e)

# Ex. 7 More Printing

# Using a .format
print("Mary had a little lamb.")
print("Its fleece was white as {}." .format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd they do?

end1 = "C"
end2 = "h"
end3= "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# what end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# Ex. 8 Printing, Printing

# assigning a string to a variable
formatter = "{} {} {} {}"

# printing the formatted variable multiple ways: int, strings, booleans, variable, nested strings
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "This is an example",
    "making up words",
    "Maybe a poem",
    "Or a song about love"
))

# Ex. 9 Printing, Printing, Printing

# shows a string on one line
days = "Mon Tue Wed Thu Fri Sat Sun"
# shows a string on new line with '\n'
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# added in variable after quotes
print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# Ex. 10 What Was That?

# tabbed in with \t
tabby_cat = "\tI'm tabbed in."
# splitting line with \n
persian_cat = "I'm split\non a line."
# showing a backslash with double \\
backslash_cat = "I'm \\ a \\ cat."
# using triple quotes to write multiple lines
# using \t to tab in the list
# tabs in and starts a new name with \t and \n
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Ex. 11 Asking Questions

# end=' ' tells python to not end the line
print("How old are you?", end=' ')
# this variable allows the user to input a response
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
# used f-string formatting to insert user's responses in the string.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Ex. 12 Prompting People

# putting a string inside of a prompt
age = input("How old are you? ")
height = input("How tall are you ")
weight = input("How much do you weight? ")
# using f-string to format the final prompt
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
