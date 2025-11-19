from utils import generate_data, process_number, timer

import multiprocessing


def worker(nums, queue):
    for num in nums:
        result = process_number(num)
        queue.put(result, block=False)  # Пытаемся добавить в очередь без блокировки


@timer
def multiprocessing_process(n):
    count_processes = multiprocessing.cpu_count()
    nums = generate_data(n)
    queue = multiprocessing.Queue()

    chunk_size = len(nums) // count_processes
    processes = []

    for i in range(count_processes):
        start_index = i * chunk_size
        end_index = (
            (i + 1) * chunk_size if i < (count_processes - 1) else len(nums)
        )  # Последний процесс берет остаток
        chunk = nums[start_index:end_index]

        process = multiprocessing.Process(target=worker, args=(chunk, queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    return None


if __name__ == "__main__":
    multiprocessing_process(n=100)
