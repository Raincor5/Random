print("Give me two numbers, I'll divide them")
print("Type 'q' quit")

while True:
    first_no = input("\n\tFirst number: ")
    if first_no == 'q':
        break
    second_no = input("\n\tSecond number: ")
    if second_no == 'q':
        break
    try:
        answer = int(first_no) / int(second_no)
    except ZeroDivisionError:
        print("Can't divide by 0")
    except ValueError:
        print("Please enter integers!")
    else:
        print(answer)