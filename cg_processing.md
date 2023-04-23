# Complete Guide - Multiprocessing
https://superfastpython.com/multiprocessing-in-python/

## Python Processes

Python provides real system-level processes via the **multiprocessing.Process** class in the **multiprocessing** module.

A Python process may progress through three steps of its life cycle:
- a new process
- a running process
- a terminated process

## Run a Function in a Process

To run a function in another process:
1. Create an instance of the `multiprocessing.Process` class.
2. Specify the name of the function via the `target` argument.
3. Call the `start()` function.

## Extend the Process Class

Instance variable attributes can be shared between processes via the `multiprocessing.Value` and `multiprocessing.Array` classes.

## Multiprocessing Pipe

In multiprocessing, a pipe is a connection between two processes in Python.

Under the covers, a pipe is implemented using a pair of connection objects, provided by the `multiprocessing.connection.Connection` class.

Creating a pipe will create two connection objects, one for sending data and one for receiving data. A pipe can be configured to be duplex so that each connection object can both send and receive data.

## Multiprocessing Queue

Python provides a process-safe queue in the `multiprocessing.Queue` class.

## Best Practices

- Use Context Managers
- Use Timeouts When Waiting
- Use Main Module Idiom
- Use Shared ctypes
- Use Pipes and Queues