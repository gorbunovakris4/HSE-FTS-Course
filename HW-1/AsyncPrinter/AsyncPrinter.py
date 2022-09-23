from threading import current_thread
from threading import Condition
from threading import Thread
from time import sleep

NUMBER_OF_THREADS = 3
SLEEP_TIME = 0.005

def printer(number, count, condition):
    with condition:
        for _ in range(count):
            for _ in range(number):
                condition.wait()
            print(number, end='')
            for _ in range(NUMBER_OF_THREADS - number):
                condition.wait()

def notifier(iterations, condition):
    for _ in range(NUMBER_OF_THREADS * iterations):
        with condition:
            condition.notify_all()
        sleep(SLEEP_TIME)

def run():
    iterations = int(input('Please, provide number of iteration: '))
    condition = Condition()
    for i in range(NUMBER_OF_THREADS):
        number = i + 1
        Thread(target=printer, args=(number, iterations, condition)).start()
    Thread(target=notifier, args=(iterations, condition)).start()

run()