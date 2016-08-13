import queue
import threading
import time

exit_flag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting "+self.name+" {0:s}".format(time.ctime(time.time())))
        process_data(self.name, self.q)
        print("Exiting "+self.name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("{0:s} processing {1:s} {2:s}".format(thread_name, data, time.ctime(time.time())))
        else:
            queue_lock.release()
        time.sleep(1)  # Leave some chance for other threads

thread_list = ["Thread-0", "Thread-1", "Thread-2"]
name_list = ["data1", "data2", "data3", "data4", "data5"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
threadID = 0

# Create new threads
for t_name in thread_list:
    thread = MyThread(threadID, t_name, work_queue)
    thread.start()
    threads.append(thread)
    threadID += 1

print(threading.current_thread())

print("Work queue empty")
# Fill the queue
queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()
print("Work queue full")

# Wait for queue to empty
while not work_queue.empty():
    pass

# Notify threads it's time to exit
exit_flag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting main thread")
