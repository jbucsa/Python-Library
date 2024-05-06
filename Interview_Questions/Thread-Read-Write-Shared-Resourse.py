"""
Here's anexample of a lock using the threading module in Python, demonstrating a scenario where a thread reads and writes to a shared resource (a file) while ensuring data integrity:    
"""

import threading
import os

class FileSafeWriter:
    def __init__(self, filename):
        self.filename = filename
        self.lock = threading.Lock()

    def write_data(self, data):
        with self.lock:  # Acquire lock before file operations
            # Check if file exists (optional for robustness)
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as file:
                    file.write("")  # Create an empty file
            # Now that the file exists, append data
            with open(self.filename, "a") as file:
                file.write(data + "\n")  # Append data with a newline

# Example usage
writer = FileSafeWriter("shared_data.txt")

def write_thread():
    for i in range(5):
        data = f"Thread data: {i}\n"
        writer.write_data(data)

threads = []
for _ in range(2):  # Create 2 threads
    thread = threading.Thread(target=write_thread)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

print("Finished writing data to the file.")


"""
Explanation:

    1. We define a FileSafeWriter class that takes a filename as input.
    2. It has a lock attribute using threading.Lock.
    3. The write_data method acquires the lock with a with statement.
    4. Inside the with block, it checks if the file exists (optional for robustness).
    5. If the file doesn't exist, it creates an empty file.
    6. Regardless of existence, it opens the file in append mode ("a") and writes the provided data with a newline character.
    7. We create a FileSafeWriter object and define a write_thread function.
    8. This function writes different data strings to the file five times (demonstrating concurrent writes).
    9. We create two threads, each calling write_thread.
    10. All threads are started and joined to ensure completion.
    11. Finally, we print a message indicating the completion of writing to the file.

Synchronization Ensures Data Integrity:
    The lock mechanism ensures that only one thread accesses the file at a time. This prevents scenarios where multiple threads might try to write data simultaneously, potentially leading to data corruption or incomplete writes. The lock guarantees a consistent writing order, resulting in a correctly formatted file with each thread's data appended sequentially.

"""