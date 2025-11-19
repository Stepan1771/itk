import time

import random

from typing import List, Tuple


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        result_time = time.time() - start
        print(f"Func: '{func.__name__}', time: {result_time}")

    return wrapper


def generate_data(
    n: int,
) -> List[int]:
    nums = [random.randint(1, 1000) for _ in range(1, n + 1)]
    print(f"nums: {nums}")
    return nums


def process_number(
    num: int,
) -> Tuple[int, bool]:
    print("start process_number", num)
    if num < 2:
        return num, False

    is_prime = True
    for divider in range(2, num):
        if num % divider == 0:
            is_prime = False
            break
    print("stop process_number", num)
    return num, is_prime
