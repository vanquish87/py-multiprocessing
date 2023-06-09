import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second.....')
    time.sleep(1)
    print('done sleeping')



if __name__ == '__main__': 
    
    processes = []
    # start lot of processes ek saath
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    # join method will help to finish processes before the end of script
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round((finish - start), 2)} Seconds(s)')