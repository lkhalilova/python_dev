term = int(input("Enter a term here: "))

# task_number_one


def fib(n):
    a, b = 0, 1
    for item in range(n + 1):
        yield a
        a, b = b, a + b


fib_generator = fib(term)
lst_generator = list(fib_generator)
print(lst_generator[-1])

# task_number_two


class FibIterator:
    def __init__(self, term_index):
        self.term_index = term_index
        self.cur_fib = 0
        self.next_fib = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.term_index == 0:
            raise StopIteration
        self.term_index -= 1
        next_fib = self.cur_fib + self.next_fib
        self.cur_fib = self.next_fib
        self.next_fib = next_fib
        return self.cur_fib


iter_fib = FibIterator(term)
lst_iter_fib = list(iter_fib)
print(lst_iter_fib[-1])

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

