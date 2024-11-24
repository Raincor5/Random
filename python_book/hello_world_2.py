#### Using a while loop with lists and dictionaries ####

# Moving items from one list to another

# Start with users that need to be verified
# and empty list to hold confirmed users.
unconfirmed_users = ["bob", "alice", "josh", "peter"]
confirmed_users = []

# Verify each user until there's no unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user {current_user.title()}...")
    confirmed_users.append(current_user)

# Display all confirmed_users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing all instances fo specific value from the list
pets = ["dog", "cat", "cat", "sobaka", "axolotl", "dog", "dog", "goldfish", "cockroach", "dog"]
print(pets)

while "dog" in pets:
    pets.remove("dog")

print(pets)


# Filling a dictionary with users' input
responses = {}
polling_active = True
while polling_active:
    name = input("Please, enter your name: \n")
    response = input("Do you like Vladimir Vladimirovic Putin's presidency style?")

    if "no" in response or "No" in response:  # Should use regex here
        # Store the response in the dictionary
        responses[name] = {"response": response,
                           "execute?": "Yes"}
    elif "Yes" in response or "yes" in response:  # Should use regex here
        responses[name] = {"response": response,
                           "execute?": "No"}


    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like another person to respond? Yes/No\n")
    if "no" in response or "No" in response:
        polling_active = False

# Polling is complete. Show the results.
print("\n---Poll Results----")
for name, response in responses.items():
    print(f"{name}'s response is:\n\t{response['response']}")
    print(f"Should we execute them?\n\t{response['execute?']}")
