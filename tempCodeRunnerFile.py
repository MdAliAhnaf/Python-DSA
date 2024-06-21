# Queues (double ended queue)
from collections import deque

queue = deque()

print(queue) #empty queue

queue.append(1) #enqueue
queue.append(2)
queue.append(3)

print(queue)

#unlike stack benefit here is, popping from left (do this operation in constant time unlike with a stack)
queue.popleft() #pops the first one which got in the list (pop from the left)

print(queue)

#queue.append(1) #enqueue
queue.appendleft(1) #double ended queue (add from the left)

print(queue)

queue.pop() #pops the last one like stack (pop from the right)
print(queue)