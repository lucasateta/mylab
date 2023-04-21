# Async IO in Python

Async IO is a concurrent programming design that has recived dedicated support in Python.

## The 10,000-Foot View of Async IO

Async IO is a single-threaded, single-process design: it uses cooperative multitasking. It is a style of concurrent programming, but it is not parallelism. It is more aligned with threading than with multipleprocessing, but is very much distinct from both of these and is a standalone member in concurrency's bag of tricks.

## Async IO is not Easy

"Use async IO when you can; use threading when you must"

At the heart of async IO are coroutines.

## APIs

asyncio provides a set of high-level APIs to:
- run Python coroutines concurrently and have full control over their execution
- perform network IO and IPC
- control subprocesses
- distribute tasks via queues
- synchronize concurrent code

Additionally, there are low-level APIs for library and framework developers to:
- create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc;
- implement efficient protocols using transports;
- brideg callback-based libraries and code with async/await syntax

### High-level APIs

#### Runners

They are built on top of an event loop with the aim to simplify async code usage for common wide-spread scenarios.

- `asyncio.run(coro, *, debug=None)` - Execute the coroutine coro and return the result.

This function runs the passed coroutine, taking care of managing the asyncio event loop, finalizing asyncrhonous generators, and closing the threadpool.

This function cannot be called when another asyncio event loop is running in the same thread.

This function always creates a new event loop and closes it at the end.

- *class* `asyncio.Runner(*, debug=None, loop_factory=None)` - Runner context manager

A context manager that simplifies *multiple* async function calls in the same context.


- Handling Keyboard Interruption

When `signal.SIGINT` is raised by Ctrl-C, KeyboardInterrupt exception is raised in the main thread by default.

#### Coroutines and Tasks

Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. To actually run a coroutine, asyncio provides the following mechanisms:
- The `asyncio.run()` function to run the top-level entry point "main()" function
- Awaiting on a coroutine.
- The `asyncio.create_task()` function to run coroutines concurrently as asyncio `Tasks`.
- The `asyncio.TaskGroup` class provides a more modern alternative to `create_task()`.

We say that an object is an awaitable if it can be used in an await expression. There are three main types of awaitable objects: coroutines, Tasks, and Futures
- Coroutines
- Tasks are used to schedule coroutines concurrently
- Futures - A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.

#### Streams

???

#### Synchronization Primitives

- asyncio primitives are not thread-safe, therefore they should not be used for OS thread synchronization (use threading for that);
- methods of these synchronization privitives do not accept the timeout argument; use the asyncio.wait_for() function to perform operations with timeouts

asyncio has the following basic synchronization primitives:
- class asyncio.Lock: implements a mutex lock for asyncio tasks. Not thread-safe.
- class asyncio.Event
- class asyncio.Condition
- class asyncio.Semaphore
- class asyncio.BoundedSemaphore
- class asyncio.Barrier
- exception asyncio.BrokenBarrierError

#### Subprocesses

This section describes high-level async/await asyncio APIs to create and manage subprocesses

#### Queues

asyncio queues are designed to be similar to classes of the queue module. asyncio queues are not thread-safe.

- class asyncio.Queue
- class asyncio.PriorityQueue
- class asyncio.LIFOQueue

Queues can be used to distribute workload between several concurrent tasks.

#### Exceptions

- `asyncio.TimeoutError`
- `asyncio.CancelledError`
- `asyncio.InvalidStateError`
- `SendfileNotAvailableError`
- `IncompleteReadError`
- `asyncio.LimitOverrunError`

### Low-level APIs

#### Event Loop

The event loop is the core of every asyncio application. Event loop run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

This section is intended mostly for authors of lower-level code, libraries, and frameworks, who need finer control over the event loop behavior.

- `asyncio.get_running_loop()`: return the running event loop in the current OS thread.

#### Callback Handles

- `asyncio.Handle`
- `asyncio.TimerHandle`

#### Server Objects

- `asyncio.Server`

#### Event Loop Implementations

- `asyncio.SelectorEventLoop`: used on Unix
- `asyncio.ProactorEventLoop`: used on Windows

### Futures

Future objects are used to bridge low-level callback-based code with high-level async/await code.

A Future represents an eventual result of an asynchronous operation. Not thread-safe.

Typically Futures are used to enable low-level callback-based code to interoperate with high-level async/await code.

