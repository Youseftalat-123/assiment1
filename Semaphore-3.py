import threading

sem = threading.Semaphore(2)

def access_resource():
    sem.acquire()
    print("Accessing resource")
    sem.release()

threads = [threading.Thread(target=access_resource) for _ in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()
