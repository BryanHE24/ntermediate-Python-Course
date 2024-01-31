from threading import Thread
import os

# random function for the example
def square_numbers():
    for i in range(100):
        i * i

# set the threads
if __name__ == "__main__":
    threads = []
    num_threads = 10

# create processes
for i in range(num_threads):
    t = threads (target=square_numbers)
    threads.append(t)
# start
    t.start()  

# wait for all processes to finish
for t in threads:
    t.join()

print('End main')