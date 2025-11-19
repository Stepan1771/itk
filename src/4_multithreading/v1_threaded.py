from concurrent.futures import ThreadPoolExecutor

from utils import generate_data, process_number, timer


@timer
def threaded(
    n: int,
    max_workers: int,
):
    nums = generate_data(n)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_number, nums)

    return None


if __name__ == "__main__":
    threaded(
        n=100000,
        max_workers=8,
    )
