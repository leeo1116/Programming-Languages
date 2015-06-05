__author__ = 'Liang Li'

# Use list as stack
lst = [12, 'asd', [12, 'asd'], {"age": 10, "letter": 'a'}]
lst.append(10)
lst.append('a')
print(lst)
lst.pop()
lst.pop()
print(lst)

# Use list as queue
