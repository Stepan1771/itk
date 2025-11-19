import json
import os.path
import random
import time
from typing import List, Tuple


def timer_saver(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        result_time = time.time() - start

        if not os.path.exists("results.json"):
            with open("results.json", "w") as json_file:
                json.dump(
                    [{"func": func.__name__, "n": result, "time": result_time}],
                    json_file,
                    indent=4,
                )

        else:
            with open("results.json", "r+") as json_file:
                data = json.load(json_file)
                data.append({"func": func.__name__, "n": result, "time": result_time})
                json_file.seek(0)
                json.dump(
                    data,
                    json_file,
                    indent=4,
                )
                json_file.truncate()

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
