import queue

L = queue.Queue(maxsize=20)

L.put(5)
L.put(8)
L.put(9)
L.put(6)
print(L)
print(L.get())
print(L.get())
