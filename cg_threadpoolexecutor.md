# Complete Guide - ThreadPoolExecutor

https://superfastpython.com/threadpoolexecutor-in-python/

The Python ThreadPoolExecutor allows you to create and manage thread pools, and it is provided in the `concurrent.futures` module.

The `ThreadPoolExecutor` extends the Executor class and will return `Future` objects when it is called.

The `Executor` class defines three methods used to control our thread pool:
- `submit()`: Dispatch a function to be executed and return a future object
- `map()`: Apply a function to an iterable of elements
- `shutdown()`: Shut down the executor

The `Future` object provides a number of method:
- `cancelled()`: Returns True if thhe task was cancelled before being executed
- `running()`
- `done()`
- `result()`
- `exception()`
- `add_done_callback()`

## ThreadPoolExecutor Usage Patterns

- Map and Wait Pattern
- Submit and Use as Completed Pattern
- Submit and Use sequentially Pattern
- Submit and Use Callback Pattern
- Submit and Wait for All Pattern
- Submit and Wait for First Pattern

## Life-Cycle of a Future Object

- Create - executor.submit(...)
- Scheduled - running() == False
- Running - running() == True
- Cancelled - cancel(), cancelled() == True
- Exception - exception() != None
- Done - done() == True, running() == False

## ThreadPoolExecutor Best Practices

- Use the Context Manager
- Use map() for Asynchronous For-Loops
- Use submit() with as_completed()
- Use Independent Functions as Tasks
- Use for IO-Bound Tasks


