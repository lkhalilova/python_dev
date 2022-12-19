password = input("Enter your password:")


if password.isdigit():
    password = int(password)

    def is_even(x):
        return x % 2 == 0

    if is_even(password):
        print(str(password) + " is even digit")
    else:
        print(str(password) + " is odd digit")
else:
    print(password + " is a word that consists of " + str(len(password)) + " letters")