term = int(input("Enter a term here: "))

# task_number_one


def fib(n):
    a, b = 0, 1
    for item in range(n + 1):
        yield a
        a, b = b, a + b


fib_generator = fib(term)
for item in fib_generator:
    pass
print(item)

# task_number_two


class FibIterator:
    def __init__(self, term_index):
        self.term_index = term_index

    def __iter__(self):
        return self

    def __next__(self):
        a, b = 0, 1
        for item in range(self.term_index):
            a, b = b, a + b
        return a


iter_fib = FibIterator(term)
print(next(iter_fib))

# task_number_3


def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


for item in range(term + 1):
    fib_recursion(item)

print(fib_recursion(item))

# task_number_4
digit = int(input("Enter a digit here: "))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(digit))

