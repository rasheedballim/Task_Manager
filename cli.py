import time


from functions import read_list, write_to_file
# or you can just say 'import functions' and then everytime you call read list or write to file,
# it must be done called as a method. eg. functions.read_list etc where 'functions' is now called a module


list = []
time_date = time.strftime("Date: %d %b %y Time: %H:%M:%S")
while True:
    print(f"It is currently \n{time_date}")
    user_action = input("Type add, show, edit or 0 to exit:  ")
    user_action = user_action.strip() +'\n'
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        list = read_list('list.txt')

        list.append(todo.title())

        write_to_file(list,'list.txt')

    elif user_action.startswith("show"):
        list = read_list('list.txt')

        # OR YOU CAN SAY "New_list = [item.strip("\n") for item in list]"
            # this is known as list comprehension
        new_list = []
        for item in list:
            new_item = item.strip("\n")
            new_list.append(new_item)

        for index, item in enumerate(new_list):
            print(f"{index + 1} -{item}")

    elif user_action.startswith("edit"):
        user_number = int(user_action[5:])
        user_number = user_number - 1

        list = read_list('list.txt')

        user_new = input("Enter a new item to do: ")
        list[user_number] = user_new + "\n"

        write_to_file(list,'list.txt')

        print(list)

    elif user_action.startswith("clear list"):
        list = read_list('list.txt')
        list.clear()
        write_to_file(list,'list.txt')

    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:]) -1
            list = read_list('list.txt')

            print(list[number])
            list.pop(number)

            write_to_file(list, 'list.txt')



        except IndexError:
            print("Value out of range!")
            continue






    elif '0' in user_action:
        break

    else:
        print("Command not valid!")

print("Done!")