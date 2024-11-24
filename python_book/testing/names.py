from name_function import get_formatted_name

print("Eneter q at any time to quit")
while True:
    first = input("\nEnter your first name > ")
    if first == "q":
        break
    last = input("\nEnter your last name > ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")