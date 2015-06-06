__author__ = 'Liang Li'
from collections import deque
# Use list as stack
lst = [12, 'asd', [12, 'asd'], {"age": 10, "letter": 'a'}]
lst.append(10)
lst.append('a')
print(lst)
lst.pop()
lst.pop()
print(lst)

# Use list as queue
queue = deque(["Alice", "Boc", "Evil"])
queue.append("Liang")
queue.append("Li")
print(queue)
queue.popleft()
print(queue)

# List comprehensions / literals
sqr = []
for x in range(10):
    sqr.append(x**2)
print(sqr)

sqr = list(map(lambda x: x**2, range(10)))
print(sqr)
sqr = [x**2 for x in range(10)]
print(sqr)
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

freshfruit = [' banana', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])