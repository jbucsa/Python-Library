"""
Accepting Locks in Python: Threading, Synchronization, and Avoiding Race Conditions

    In Python, when you work with multiple threads accessing shared resources (like variables, files, or external connections), you encounter the risk of race conditions. A race condition occurs when the outcome of your program depends on the unpredictable timing of thread execution, leading to unexpected or incorrect behavior.

Understanding Threading

    Threading is a technique that allows a program to execute multiple independent sequences of instructions (threads) concurrently. This enables tasks to run seemingly in parallel, improving responsiveness and potentially speeding up execution. However, it requires careful handling of shared resources to avoid race conditions.

Synchronization Primitives: Locks and Mutexes

    To ensure data consistency and prevent race conditions in multi-threaded programs, Python provides synchronization primitives. These mechanisms control access to shared resources, guaranteeing that only one thread modifies the resource at a time.
        Locks: Locks are fundamental synchronization primitives. They act like a mutual exclusion (mutex) mechanism, allowing only one thread to acquire (lock) the resource at a time. Other threads attempting to access the same resource will be blocked until the lock is released.

Using Locks in Python: The threading Module

    The threading module in Python offers various lock implementations:
        threading.Lock: This is a basic binary lock. It's either acquired (lock.acquire()) or not. Attempting to acquire a locked resource blocks the thread until it's released (lock.release()).
"""

import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # Acquire lock before modifying count
            self.count += 1

    def get_count(self):
        with self.lock:  # Acquire lock before reading count
            return self.count

# Create a counter and multiple threads to increment it
counter = Counter()

def incrementing_thread():
    for _ in range(10000):
        counter.increment()

threads = []
for _ in range(4):  # Create 4 threads
    thread = threading.Thread(target=incrementing_thread)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

print("Final count:", counter.get_count())  # Should be 40000

"""
Explanation:

    1. We define a Counter class with count and a lock attribute.
    2. The increment method acquires the lock using a with statement, ensuring the lock is released even if an exception occurs.
    3. Inside the with block, count is incremented.
    4. The get_count method similarly acquires the lock before reading count.
    5. We create a counter and multiple threads, each calling incrementing_thread to increment the counter 10000 times.
    6. incrementing_thread acquires the lock, increments count, and releases the lock.
    7. Threads are started (thread.start()) and then joined (thread.join()) to wait for their completion.
    8. Finally, the get_count method (with lock acquisition) is used to print the final counter value, which should be 40000 (4 threads * 10000 increments each).

Additional Synchronization Primitives:

    threading.RLock: A reentrant lock allows the same thread to acquire the lock multiple times without blocking itself. Useful for scenarios where a thread might recursively call functions that require the lock.
    Semaphores: These control access to a limited number of resources. A thread attempting to acquire a semaphore that has reached its limit will be blocked until a resource becomes available.
    Condition variables: These allow threads to wait for specific conditions to be met before proceeding.

By understanding threading, synchronization primitives like locks, and using them effectively, you can prevent race conditions and ensure data consistency in multi-threaded Python applications.

"""