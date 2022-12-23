# task_number_1

text = input("Enter some text here ")


for symbol in text:
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            print(f"{symbol} is an even digit")
        else:
            print(f"{symbol} is an odd digit")

    elif symbol.isalnum():
        if symbol.isupper():
            print(f"{symbol} is an uppercase letter")
        else:
            print(f"{symbol} is a lowercase letter")
    else:
        print(f"{symbol} is a symbol")

# task_number_two

import time

while True:
    print("I love Python")
    time.sleep(4.2)
    continue