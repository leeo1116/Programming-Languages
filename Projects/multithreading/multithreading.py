import threading
import time

exit_flag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting "+self.name+" {0:s}".format(time.ctime(time.time())))
        print_time(self.name, self.delay, 5)
        print("Exiting "+self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print("{0:s}: {1:s}".format(thread_name, time.ctime(time.time())))
        counter -= 1

# Create 2 new threads
thread0 = MyThread(0, "Thread-0", 3)
thread1 = MyThread(1, "Thread-1", 2)

# Start threads
thread0.start()
thread1.start()

print("Exiting main thread")
