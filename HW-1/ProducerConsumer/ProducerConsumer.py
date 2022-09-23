from threading import Condition
from threading import Thread
from queue import Queue
from random import randint
from time import sleep

global_queue = Queue()
RAND_COUNT = 3
RAND_SLEEP = 5
SLEEP_TIME = 0.005

def producer(number, condition):
    while True:
        sleep(randint(1, RAND_COUNT))

        count = randint(1, RAND_COUNT)
        print(f"{number}-th producer published {count} available products")

        for _ in range(count):
            global_queue.put(number)
            with condition:
                condition.notify_all()
            sleep(SLEEP_TIME)

        print()


def consumer(number, condition, consumers):
    while True:
        for _ in range(number):
            with condition:
                condition.wait()

        producer_number = global_queue.get()

        print(f"{number}-th consumer received product from {producer_number}-th producer")

        for _ in range(consumers - number):
            with condition:
                condition.wait()

def run():
    count_consumers = int(input("Please, provide the number of consumers: "))
    count_producers = int(input("And producers: "))
    
    condition = Condition()

    for i in range(count_consumers):
        Thread(name=str(i + 1), target=consumer, args=(i + 1, condition, count_consumers)).start()
    for i in range(count_producers):
        Thread(name=str(i), target=producer, args=(i + 1, condition)).start()

run()