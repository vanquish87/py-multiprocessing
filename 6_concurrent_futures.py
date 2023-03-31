import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} seconds.....')
    time.sleep(seconds)
    return 'done sleeping...'


if __name__ == '__main__': 

    # using with context manager
    with concurrent.futures.ProcessPoolExecutor() as executer:
        f1 = executer.submit(do_something, 1)
        f2 = executer.submit(do_something, 1)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f'Finished in {round((finish - start), 2)} Seconds(s)')