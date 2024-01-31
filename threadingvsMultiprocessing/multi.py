from multiprocessing import Process
import os

#
def square_numbers():
    for i in range(100):
        i * i

#
processes = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)
# start
    p.start()  

# wait for all processes to finish
for p in processes:
    p.join()

print('End main')