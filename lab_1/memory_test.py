from sys import getsizeof

a = []
print(str(a), getsizeof(a))
a = [0]
print(str(a), getsizeof(a))
a = [0, 0, 0, 0, 0]
print(str(a), getsizeof(a))
a = [[],[]]
print(str(a), getsizeof(a))
a = 1
print(str(a), getsizeof(a))
a = str('')
print(str(a), getsizeof(''))
