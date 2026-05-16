#opposite of a stack, first in first out. Like a litearl queue in a line, first in the line is the first to leave the line. 
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

print("---------")
x = queue.popleft()
print(x)
print(queue)
#removes from the front like a line basically

print("---------")
queue.append(50)
print(queue)
#adding to the queue like a stack/list but we use operations like popleft to manipulate it like a irl queue