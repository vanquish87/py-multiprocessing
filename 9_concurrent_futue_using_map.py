import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} seconds.....')
    time.sleep(seconds)
    return f'done sleeping {seconds} ...'

# see in which sequence processes are called and returned
if __name__ == '__main__': 

    seconds = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # using with context manager
    with concurrent.futures.ProcessPoolExecutor() as executer:
        # map function will run on all the iterable of list
        # map will return results unlike submit method from previous 8_concurrent.py
        # it will give results as they are started till then it just waits
        results = executer.map(do_something, seconds)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round((finish - start), 2)} Seconds(s)')