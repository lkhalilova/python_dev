import re

# task_num_1
phone_book = {
    "Alina Kravchenko": "0664686501",
    "Egor Miroshnichenko": "0995678456",
    "Ruslan Volikov": "0987656342",
    "Nastya Lehenka": "0995676456"

}
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
            number_val = re.fullmatch(r"(\+)?(38)?0\d{9}", split_input[3])
            if number_val:
                new_contact = [new_name, split_input[3]]
                phone_book.update({new_contact[0]: new_contact[1]})
            else:
                print("The number is not valid")
        else:
            print("the contact already exists")

    elif "delete" in user_input:  # format: "delete full name"
        key = split_input[1].title() + " " + split_input[2].title()
        if phone_book.get(key) is not None:
            del phone_book[key]
        else:
            print("the contact has not been found")


# task_num_2
file_name = input("Enter a name of a file here: ")
with open(file_name, "w") as file:
    file.write("There are a couple lolitakhalilova1201@gmail.com of emails in this liudmyla_lehenka22@gmail.com text.")

with open(file_name, "r") as file:
    read_file = file.read()
    new_file = re.sub("\w+@gmail\.com", "*@*", read_file)

with open(file_name, "w") as file:
    file.write(new_file)

# task_num_3
file_name = input("Enter a name of a file here: ")
with open(file_name, "w") as file:
    file.write("There are a couple lolitakh12@gmail.com of emails in this "
               "masha_lehenka@gmail.com text robdreams@gmail.com")

with open(file_name, "r") as file:
    read_file = file.read()
    iter_file = re.finditer(r"\S+", read_file)
    lst = []
for item in iter_file:
    if re.match("\w+@\S+", item.group()):
        res = f"{item.group()[0]}***@***{item.group()[-1]}"
        lst.append(res)
    else:
        lst.append(item.group())

new_text = " ".join(lst)

with open(file_name, "w") as file:
    file.write(new_text)

