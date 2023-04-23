# Complete Guide - Threading
https://superfastpython.com/threading-in-python/

The **Python Threading** module allows you to create and manage new threads of execution in Python.

## Python Threads

A thread refers to a thread execution in a computer program.

A Python thread is an object representation of a native thread provided by the underlying operating system.

## Run a Function in a Thread

When we create and run a new thread, Python will make system calls on the underlying operating system and request a new thread be created and to start running the new thread.

A thread in Python is represented as an instance of the `threading.Thread` class. A Python thread may progress through three steps of its life-cycle:
- New Thread
- Running Thread
  * Blocked Thread (Optional)
- Terminated Thread

## Extend the Thread Class

We can also execute functions in another thread by extending the `threading.Thread` class and overriding the `run()` function.

## Thread Instance Attributes

### Query Thread Name

## Configure Threads

## Main Thread

## Thread Utilities

## Thread Exception Handling

## Limitations of Threads in Python

The CPython Python interpreter uses a mutual exclusion (mutex) lock within the interpreter that ensures that only one thread at a time can execute Python bytecodes in the Python virtual machine. This lock is referred to as the Global Interpreter Lock or GIL for short.

## When to Use a Thread

There are times when the lock is released by the interpreter and we can achieve parallel execution of our concurrent code in Python. Examples of when the lock is released include:
- When a thread is performing blocking IO.
- When a thread is executing C code and explicitly releases the lock.

## Thread Blocking Calls

There are three types of blocking function calls we need to consider in concurrent programming:
- Blocking calls on concurrent primitives
  - threading.Lock.acquire()
  - threading.Condition.wait()
  - threading.Thread.join()
  - threading.Semaphore.acquire()
  - threading.Event.wait()
  - threading.Barrier.wait()
- Blocking calls for IO
  - hard disk drive: reading, writing, etc.
  - Peripherals: mouse, keyboard, serial, camera, etc.
  - Internet
  - Database
- Blocking calls to Sleep

## Thread-Local Data

Threads can store local data via an instance of the `threading.Local` class.

## Thread Mutex Lock

## Thread Reentrant Lock

A thread may need to acquire the same lock more than once. Each time a thread acquires the lock it must also release it, meaning that there are recursive levels of acquire and release for the owning thread.

## Thread Condition

In concurrency, a condition (also called a monitor) allows multiple threads to be notified about some result.

It combines both a mutual exclusion lock (mutex) and a conditional variable.

By default, a condition object will create a new reentrant mutex lock.

## Thread Semaphore

A semaphore allows a limit on the number of threads that can acquire a lock protecting a critical section

## Thread Event

An event is a thread-safe boolean flag.

## Timer Threads

## Thread Barrier

## Python Threading Best Practices

## Python Threading Common Errors

## Python Threading Common Questions

## Common Objections to Using Python Threads

## Further Reading
