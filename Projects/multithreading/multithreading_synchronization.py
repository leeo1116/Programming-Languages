import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting "+self.name+" {0:s}".format(time.ctime(time.time())))
        thread_lock.acquire()  # Get lock to synchronize threads
        print_time(self.name, self.delay, 3)
        thread_lock.release()  # Free lock to release next threads
        print("Exiting "+self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("{0:s}: {1:s}".format(thread_name, time.ctime(time.time())))
        counter -= 1

thread_lock = threading.Lock()
threads = []

# Create 2 new threads
thread0 = MyThread(0, "Thread-0", 3)
thread1 = MyThread(1, "Thread-1", 2)

# Start threads
thread0.start()
thread1.start()

# Add threads to thread list
threads.append(thread0)
threads.append(thread1)
print("Threads appending completed")

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting main thread")