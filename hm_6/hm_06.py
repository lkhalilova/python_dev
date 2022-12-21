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

    elif "show" in user_input:
        name = split_input[1] + " " + split_input[2]
        print(phone_book.get(name.title()))

    elif "add" in user_input:
        new_name = split_input[1].title() + " " + split_input[2].title()
        new_contact = [new_name, split_input[3]]
        phone_book.update({new_contact[0]: new_contact[1]})

    elif "delete" in user_input:
        key = split_input[1].title() + " " + split_input[2].title()
        del phone_book[key]





