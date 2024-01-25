from collections import deque

# Create a deque collection
d = deque()

# add elements
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

# remove the last,left,all elements
#d.pop()
#d.popleft()
#d.clear()
#print(d)

# extend it using a list of elements
d.extend([4,5,6])
print(d)