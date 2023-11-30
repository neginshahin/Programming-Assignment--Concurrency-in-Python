import multiprocessing
import time
from datetime import datetime
import random

def print_current_time(process_name):
    current_time = datetime.now()
    print(f"Process {process_name}: {current_time}")
    time.sleep(random.random())

if __name__ == '__main__':
    for i in range(3):
        process = multiprocessing.Process(target=print_current_time, args=(f"Process-{i}",))
        process.start()
        process.join()

    print('Completed')