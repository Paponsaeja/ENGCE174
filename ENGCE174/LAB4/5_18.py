# ex using list as stack and queues

# stack operating (last in, first out ) LIFO
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("popped item from stack :", popped_item)

#Queues operating FIFO

from collections import deque 
queue = deque([1,2,3])
queue.append(4)
dequeue_item = queue.popleft()
print("Dequeued item from queue: ", dequeue_item)