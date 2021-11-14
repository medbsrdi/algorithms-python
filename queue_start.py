#try out the python queue function 
from collections import deque

# create new empty queue
queue = deque()

#add some items to the queue
queue.append(2)
queue.append(5)
queue.append(8)
queue.append(78)
queue.append(3)

#print the queue content
print(queue)

#todo pop an item off the front of the queue
queue.pop()
queue.pop()
print(queue)