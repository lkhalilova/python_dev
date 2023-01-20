# task_num_1
import json
phone_book = {
    "Alina Kravchenko": "0664686501",
    "Egor Miroshnichenko": "0995678456",
    "Ruslan Volikov": "0987656342",
    "Nastya Lehenka": "0995676456"

}

json_phone_book = json.dumps(phone_book, indent=0)

with open("json_phone_book.json", "x") as file:
    file.write(json_phone_book)

count = 3

while count:
    user_input = input("Enter a command here: ")
    split_input = user_input.split()

    if user_input == "stats":
        contacts_amount = len(phone_book)
        print(contacts_amount)

    elif user_input == "list":
        all_names = phone_book.keys()
        for name in all_names:
            print(name)

    elif "show" in user_input:  # format: "show full name"
        name = split_input[1] + " " + split_input[2]
        print(phone_book.get(name.title()))

    elif "add" in user_input:  # format: "add full name number"
        new_name = split_input[1].title() + " " + split_input[2].title()
        if phone_book.get(new_name) is None:
            new_contact = [new_name, split_input[3]]
            phone_book.update({new_contact[0]: new_contact[1]})
        else:
            print("the contact already exists")

    elif "delete" in user_input:  # format: "delete full name"
        key = split_input[1].title() + " " + split_input[2].title()
        if phone_book.get(key) is not None:
            del phone_book[key]
        else:
            print("the contact has not been found")
    count -= 1

new_json_phone_book = json.dumps(phone_book, indent=0)

with open("json_phone_book.json", "w") as file:
    file.write(new_json_phone_book)

with open("json_phone_book") as file:
    read_file = file.read()
    print(type(read_file))
    print(json.loads(read_file))

# task_num_2
import datetime
import math


def get_time_and_name(func):
    def inner(*args, **kwargs):
        call_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(f"function {func} was called at {call_time}")
        with open("decorated_functions.txt", "a") as file:
            file.write(f"function {func} was called at {call_time}\n")
        return result
    return inner


@get_time_and_name
def factorial(num):
    print(math.factorial(num))


print(factorial(8))

# task_num_3


class MyCustomException(Exception):
    print("Custom exception is occurred")
    exception_time = datetime.datetime.now()
    with open("exceptions.txt", "a") as file:
        file.write(f"Exception occurred at {exception_time}\n")


try:
    raise MyCustomException()
except MyCustomException:
    pass

