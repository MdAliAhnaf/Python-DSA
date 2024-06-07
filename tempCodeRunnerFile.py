# Queues (double ended queue)
from collections import deque

queue = deque()

print(queue) #empty queue

queue.append(1) #enqueue
queue.append(2)
queue.append(3)

print(queue)

# queue.pop() #pops the last one like stack

queue.popleft() #pops the first one which got in the list

print(queue)

#queue.append(1) #enqueue
queue.appendleft(1)

print(queue)

queue.pop()
print(queue)
