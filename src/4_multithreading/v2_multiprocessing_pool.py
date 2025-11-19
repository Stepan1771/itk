import multiprocessing

from utils import generate_data, process_number, timer


@timer
def multiprocessing_pool(
    n: int,
):
    nums = generate_data(n)
    count_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=count_processes) as pool:
        pool.map(process_number, nums)

    return None


if __name__ == "__main__":
    multiprocessing_pool(n=1)
