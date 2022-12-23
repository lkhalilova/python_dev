phone_book = {
    "Alina Kravchenko": "0664686501",
    "Egor Miroshnichenko": "0995678456",
    "Ruslan Volikov": "0987656342",
    "Nastya Lehenka": "0995676456"

}
while True:
    user_input = input("Enter a command here: ")
    split_input = user_input.split()

    if user_input == "stats":
        contacts_amount = len(phone_book)
        print(contacts_amount)

    elif user_input == "list":
        all_names = phone_book.keys()
        for name in all_names:
            print(name)

    elif "show" in user_input:  # format "show full name"
        name = split_input[1] + " " + split_input[2]
        print(phone_book.get(name.title()))

    elif "add" in user_input:  # format "add full name number"
        new_name = split_input[1].title() + " " + split_input[2].title()
        if phone_book.get(new_name) is None:
            new_contact = [new_name, split_input[3]]
            phone_book.update({new_contact[0]: new_contact[1]})
        else:
            print("the contact already exists")

    elif "delete" in user_input:  # format "delete full name"
        key = split_input[1].title() + " " + split_input[2].title()
        if phone_book.get(key) is not None:
            del phone_book[key]
        else:
            print("the contact has not been found")






