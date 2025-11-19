from v1_threaded import threaded

from v2_multiprocessing_pool import multiprocessing_pool

from v3_multiprocessing_process_queue import multiprocessing_process


if __name__ == '__main__':
    threaded(n=1000)
    multiprocessing_pool(n=1000)
    multiprocessing_process(n=1000)