import multiprocessing

from utils import generate_data, process_number, timer_saver


@timer_saver
def multiprocessing_pool(
    n: int,
):
    nums = generate_data(n)
    count_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=count_processes) as pool:
        pool.map(process_number, nums)

    return n


if __name__ == "__main__":
    multiprocessing_pool(n=100)
