import threading
//youseftalaat
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    lock1.acquire()
    print("Thread1 acquired lock1")
    lock2.acquire()
    print("Thread1 acquired lock2")
    lock2.release()
    lock1.release()

def thread2():
    lock2.acquire()
    print("Thread2 acquired lock2")
    lock1.acquire()
    print("Thread2 acquired lock1")
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
t1.join()
t2.join()
