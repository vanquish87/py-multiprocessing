# Join method to run process ek saath without skipping them to the end

import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second.....')
    time.sleep(1)
    print('done sleeping')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()


# join method will help to finish processes before the end of script
p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round((finish - start), 2)} Seconds(s)')