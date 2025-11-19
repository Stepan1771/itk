from concurrent.futures import ThreadPoolExecutor

from utils import generate_data, process_number, timer_saver


@timer_saver
def threaded(
    n: int,
    max_workers: int = 8,
):
    nums = generate_data(n)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_number, nums)

    return n


if __name__ == "__main__":
    threaded(
        n=100,
        max_workers=8,
    )
