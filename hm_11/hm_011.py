# task_num_1
import math
import datetime


def get_time_and_name(func):
    def inner(*args, **kwargs):
        call_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(f"function {func} was called at {call_time}")
        return result
    return inner


@get_time_and_name
def factorial(num):
    print(math.factorial(num))
    return 2


print(factorial(8))

# task_num_2


class MyCustomException(Exception):
    print("Custom exception is occurred")


try:
    raise MyCustomException()
except MyCustomException:
    pass

# task_num_3


class CodeHighlight:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print(exc_type)
        print("=" * 10)
        return True


my_dict = {}

with CodeHighlight():
    print(my_dict["test"])


# task_num_4

try:
    print("=" * 10)
    print(abc)
except Exception as exc:
    print(exc)
finally:
    print("=" * 10)
