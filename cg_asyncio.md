# The Complete Guide - Python Asyncio

https://superfastpython.com/python-asyncio/

**Asyncio** allows us to use asynchronous programming with coroutine-based concurrency in Python.

## What is Asynchronous Programming

Asynchronous programming is a programming paradigm that does not block.

### Asynchronous Tasks

* **Asynchronous Function Call**: the function call will happen somehow and at some time, in the background, and the program can perform other tasks or respond to other events.
* **Future**: A handle on an asynchronous function call allowing the status of the call to be checked and results to be retrieved.
* **Asynchronous Task**: used to refer to the aggregate of an asynchronous function call and resulting future.

### Asynchronous Programming

* **Asynchronous Programming** is primarily used with non-blocking I/O, such as reading and writing from socket connections with other processes or other systems.
* **Non-blocking I/O**: performing I/O operations via asynchronous requests and responses
* **Asynchronous I/O**: A shorthand that refers to combining asynchronous programming with non-blocking I/O.

### Asynchronous Programming in Python

We can implement asyncrhonous programming in Python in various ways.

* **Asyncio**: it is implemented using coroutines that run in an event loop that itself runs in a single thread.
* **Concurrent**: multiprocessing and multithreading module
* **signal module**

## What is Asyncio

* Coroutines: is a function that can be suspended and resumed.

