from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")
while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos("todos.txt")
        todos.append(todo)
        write_todos("todos.txt", todos)
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            choice = int(user_action[5:])
            new_input = input("Enter a new value: ")

            todos = get_todos("todos.txt")

            todos.__setitem__(choice-1, new_input + "\n")  # Works the same way as todos[choice-1] = new_input

            write_todos("todos.txt", todos)

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        except Exception as e:
            print(f"Error: {e}")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            removed_item = todos[number-1]
            todos.pop(number - 1)

            write_todos("todos.txt", todos)

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")

            print(f"Todo '{removed_item.strip('\n')}' has been removed.")
        except Exception as e:
            print(f"Error: {e}")

    elif user_action.startswith("exit"):
        break
    else:  # None of the cases matched.
        print("WRONG!")

print("Bye!")
