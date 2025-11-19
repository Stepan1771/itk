import multiprocessing
import queue

from utils import generate_data, process_number, timer_saver


def worker(nums, result_queue):
    chunk_results = []
    for num in nums:
        result = process_number(num)
        chunk_results.append(result)
    result_queue.put(chunk_results)


@timer_saver
def multiprocessing_process(n):
    nums = generate_data(n)
    count_processes = min(multiprocessing.cpu_count(), len(nums))

    chunk_size = len(nums) // count_processes
    chunks = [nums[i : i + chunk_size] for i in range(0, len(nums), chunk_size)]

    processes = []
    result_queue = multiprocessing.Queue()

    for chunk in chunks:
        process = multiprocessing.Process(target=worker, args=(chunk, result_queue))
        process.start()
        processes.append(process)

    results = []
    for _ in range(len(chunks)):
        try:
            chunk_results = result_queue.get(timeout=30)
            results.extend(chunk_results)
        except queue.Empty:
            break

    for process in processes:
        process.join(timeout=5)
        if process.is_alive():
            process.terminate()

    return n


if __name__ == "__main__":
    multiprocessing_process(n=100000)
