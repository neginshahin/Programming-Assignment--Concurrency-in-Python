''' 15.1 Use multiprocessing to create three separate processes.
Make each one wait a random number of seconds between zero and one, print the current time, and then exit. '''

import multiprocessing
import time
from datetime import datetime
import random

# Function to print current time and sleep for a random duration
def print_current_time(process_name):
    current_time = datetime.now()
    print(f"Process {process_name}: {current_time}")
    time.sleep(random.random())

if __name__ == '__main__':
    # Create a loop to spawn three separate processes
    for i in range(3):
        process = multiprocessing.Process(target=print_current_time, args=(f"Process-{i}",))
        process.start()
        process.join()

    # This line will be executed after all three processes have finished
    print('Completed')
