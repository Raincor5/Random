msg = "Hello Galaxy!"
print(msg)

msg = "Hello The World and The Galaxy!"
print(msg)

# Define a function named spam
def spam():

    # Define the variable ham
    ham = "Hello World!"

    # Define the variable eggs
    eggs = 1

    return print(ham, eggs)

spam()

name = "ada lovelace"
print(name.title(), name.upper(), name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

print("Python")
print("\tPython")
print("Programming languages:\nPython\nC\nJavaScript")

favourite_language = " Python "
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

# nostarch_url = "https://nostarch.com"
# print(nostarch_url.removeprefix("https://"))
# Not working?

print(0.2+0.1)
print(3*0.1)

universal_age = 14_000_000_000
print(universal_age)

#### Lists!!! ####

bikes = ["honda", "yamaha", "suzuki"]
print(f"The bike I want is {bikes[-2]}")
bikes.insert(1, "ducati")
print(bikes)
del bikes[0]
print(bikes)
# pop() - removes the last element of the list

last_owned = bikes.pop()
print(f"The bike I last owned was {last_owned.title()}")

# Remove by value - remove()
bikes.remove("yamaha")
print(bikes)

# List comprehension
squares = [value ** 2 for value in range(1,11)]
print(squares)

# List slicing
# *list*[:4] === *list*[1:4]
# *list*[2:] === *list*[2:5] (Max 5)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[-3:])  # [5, 6, 7]
print(numbers[:-3])  # [1, 2, 3, 4]

# Copying a list
list_one = [1, 2, 3, 4, 5]
list_two = list_one[:] # Yes, : is being used

print(list_one, list_two)

# Tuples. Are a list-like object that cannot be modified, yet can be reassigned
my_t = (3,)  # A tuple with one element
print(my_t)

# In if-elif-else condition, the condition validation stops at the first if statement satisfaction.
requested_toppings = ["Mushrooms", "Extra cheese"]

if "Mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "Extra cheese" in requested_toppings:
    print("Adding extra cheese")
if "Pepperoni" in requested_toppings:
    print("Adding pepperoni")
print("\nFinished adding toppings\n")

if "Mushrooms" in requested_toppings:
    print("Adding mushrooms")
elif "Extra cheese" in requested_toppings:
    print("Adding extra cheese")
elif "Pepperoni" in requested_toppings:
    print("Adding pepperoni")
print("Finished adding toppings\n")  # Only "Adding mushrooms is printed"

# Checking if the list is not empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("Finished adding topings")
else:
    print("\nAre you sure you want a plain pizza?\n")

# Using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineaple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}")
    else:
        print(f"Sorry, we don't have {requested_topping.title()}")
print("Finished adding toppins!")


##### Dictionaries!!! #####

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium", "colour": "green", "name": "bumbukalns"}
print(f"Original position: {alien_0['x_position']}")
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"The new position is now {alien_0['x_position']}")
del alien_0["name"]
print(alien_0)

# Using get() method to access values
name_value = alien_0.get("name", "\nThe alien doesn't have a name yet\n")
print(name_value)

# Using items()
favourite_languages = {"sarah": "assembler", "david": "hebrew", "edward": "rust", "jen": "python", "slava": "python"}
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ["sarah", "david"]

# Using keys()
for name in favourite_languages.keys():
    print(f"Hi, {name.title()}!")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Using values()
print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned (without repetition):")
for language in set(favourite_languages.values()): # set() takes unique values, no using duplicates
    print(language.title())

# An example of a set
languages = {"python", "rust", "c", "java", "python"}
print("\n", languages)

# Lists in a dictionary
favourite_languages = {
    "sarah": ["python", "rust"],
    "jen": ["rust"],
    "edward": ["c"],
    "jeremy": ["assembler", "java"],
    "sean": ["javascript", "c#"]
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A dictionary in dictionary
users = {
    "aenstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },

    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


#### Working with user's input ####

# Modulo
number = input("Enter a number, I will tell you if it's even or odd\n")

if number.isnumeric():
    if int(number) % 2 == 0:
        print(f"\nThe number {number} is even.")
    elif int(number) % 2 == 1:
        print(f"\nThe number {number} is odd.")
else:
    print(f"{number} is not a number!")

# Quit the loop
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program\n"
message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)

# Using Flag to exit a loop
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program\n"

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

# Using Break to exit the loop
prompt = "\nPlease enter a city you have visited: "
prompt += "\n(Enter 'quit' to end the program)\n"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to visit {city.title()}!")

# Using Continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)