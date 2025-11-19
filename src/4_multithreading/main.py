from v1_threaded import threaded

from v2_multiprocessing_pool import multiprocessing_pool

from v3_multiprocessing_process_queue import multiprocessing_process


if __name__ == '__main__':
    n = 100
    threaded(n=n)
    multiprocessing_pool(n=n)
    multiprocessing_process(n=n)