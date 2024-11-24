#### Functions ####

# Making an argument optional
def get_fotmatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

genius = get_fotmatted_name("Nikola", "Tesla")
print(genius)

genius = get_fotmatted_name("Elon", "Musk", "Reeves")
print(genius)


# Passing arbitrary number of arguments
def make_pizza(*toppings):  # One * is an arbitrary argument
    print("\nMaking pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "cheese", "pepperonni", "peppers")

# Mixing positional and arbitrary arguments
def make_another_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_another_pizza(12, "pepperoni")
make_another_pizza(16, "mushrooms", "cheese", "pepperonni", "peppers")

# Using arbitrary keyword arguments
def build_profile(first, last, **user_info):  # Two *s is an keyword arbitrary argument
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info

user_profile = build_profile("alber", "enstein", location="princeton", field="physics")
print(user_profile)
# You can create a .py file storing different functions or classes as a library (or module) (e.g. pizza.py)
# And then use the methods (functions) from the imported module


