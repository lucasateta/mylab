from time import sleep
from random import random
import threading
from threading import Thread, current_thread, main_thread, active_count, enumerate, RLock, Event, Condition, Semaphore
import logging
from typing import List

import pytest
SLEEP_TIME=0.01
def test_thread_lifecycle():
    messages = []
    def task(sleep_time, msg):
        sleep(sleep_time)
        messages.append(msg)

    thread = Thread(target=task, args=(SLEEP_TIME, "new message"))
    thread.start()
    assert messages == []
    assert thread.is_alive() == True
    thread.join()
    assert messages == ["new message"]
    assert thread.is_alive() == False

def test_extending_thread():
    class CustomThread(Thread):
        def __init__(self):
            super().__init__()

            self.message = ''
            self.value = None

        def run(self):
            sleep(SLEEP_TIME)
            self.message = "updated message"
            self.value = 50

    thread = CustomThread()
    thread.start()
    assert thread.message == ""
    thread.join()
    assert thread.message == "updated message"
    assert thread.value == 50

def test_query_thread_name():
    thread = Thread()
    assert isinstance(thread.name, str)
    assert thread.name != ''

def test_query_thread_daemon():
    thread = Thread()
    assert thread.daemon == False
    thread = Thread(daemon=True)
    assert thread.daemon == True

def test_query_thread_id():
    thread = Thread()
    assert thread.ident is None
    thread.start()
    assert type(thread.ident) == int
    thread.join()

def test_query_thread_native_id():
    thread = Thread()
    thread.start()
    assert type(thread.native_id) == int
    thread.join()

def test_query_thread_isalive():
    thread = Thread(target=lambda: sleep(0.1))
    assert thread.is_alive() == False
    thread.start()
    assert thread.is_alive() == True
    thread.join()
    assert thread.is_alive() == False

def test_config_thread():
    thread = Thread(name="my_thread")
    assert thread.name == "my_thread"

    thread = Thread(daemon=True)
    assert thread.daemon == True
    thread.daemon = False
    assert thread.daemon == False

def test_current_thread():
    thread = current_thread()
    assert thread.name == 'MainThread'
    assert thread.daemon == False
    assert type(thread.ident) == int
    assert type(thread.native_id) == int

def test_main_thread():
    thread = main_thread()
    assert thread.name == "MainThread"

def test_query_current_thread_and_main_thread():
    def task():
        assert isinstance(current_thread(), Thread)
        assert isinstance(main_thread(), Thread)
        assert current_thread() != main_thread()
        sleep(SLEEP_TIME)

    thread = Thread(target=task)
    thread.start()
    assert isinstance(current_thread(), Thread)
    assert isinstance(main_thread(), Thread)
    assert main_thread() == current_thread()
    assert len(enumerate()) == 2
    thread.join()

def test_unhandled_exception():
    caught_exceptions = []
    def custom_hook(args):
        caught_exceptions.append(args)

    def task():
        sleep(SLEEP_TIME)
        raise Exception("something bad happened")
    
    threading.excepthook = custom_hook

    thread = Thread(target=task)
    thread.start()
    thread.join()
    assert caught_exceptions[0].exc_type == Exception
    assert caught_exceptions[0].exc_value.args[0] == "something bad happened"
    assert caught_exceptions[0].thread == thread

def test_reentrant_lock():
    results = []
    def do_something(lock, id, value):
        with lock:
            results.append(value)

    def task(lock, id, value):
        with lock:
            sleep(value)
            do_something(lock, id, value)

    lock = RLock()

    threads = []
    for i in range(10):
        t = Thread(target=task, args=(lock, i, random()/100))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert len(results) == 10

def test_condition():
    def task(condition: Condition, work_list: List):
        sleep(SLEEP_TIME)
        work_list.append(33)
        with condition:
            condition.notify()

    condition: Condition = Condition()
    work_list: List = list()
    with condition:
        worker = Thread(target=task, args=(condition, work_list))
        worker.start()
        condition.wait()

        worker.join()

    assert work_list == [33]

def test_semaphore():
    workers = []
    in_critical_section = [False] * 10
    lock = RLock()
    num = 4

    def update_in_critical_section(lock: RLock, i, is_in:bool):
        with lock:
            in_critical_section[i] = is_in

    def get_in_critical_section_count(lock: RLock):
        with lock:
            res = sum(map(lambda i: i == True, in_critical_section))
            return res

    def task(semaphore: Semaphore, i:int):
        with semaphore:
            update_in_critical_section(lock, i, True)
            value = random()
            sleep(value/100)
            assert get_in_critical_section_count(lock) <= num

            update_in_critical_section(lock, i, False)

    semaphore: Semaphore = Semaphore(num)
    for i in range(10):
        worker = Thread(target=task, args=(semaphore, i))
        worker.start()
        workers.append(worker)

    for w in workers:
        w.join()


def test_event():
    threads: List[Thread] = []
    def task(event: Event, number: int):
        event.wait()
        value = random()
        sleep(value/100)

    event = Event()
    for i in range(5):
        thread = Thread(target=task, args=(event, i))
        thread.start()
        threads.append(thread)

    event.set()
    for t in threads:
        t.join()

    assert sum(map(lambda t: t.is_alive(), threads)) == 0
    