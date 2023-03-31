import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} seconds.....')
    time.sleep(seconds)
    return f'done sleeping {seconds} ...'

# see in which sequence processes are called and returned
if __name__ == '__main__': 

    # i have 12 cores so to check how they are used and free up
    seconds = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # using with context manager
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = [executer.submit(do_something, sec) for sec in seconds]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round((finish - start), 2)} Seconds(s)')