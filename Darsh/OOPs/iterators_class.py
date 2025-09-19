# what is an iterator/iterable?
# an iterator is an object that can be iterated upon, meaning that you can traverse through all its elements
# an iterable is an object that defines an __iter__ method, returning an iterator object

#region examples
# l = [1, 2, 3, 4, 5]
# i = iter(l)
# print(i)
#
# for x in l:
#     print(x)
#
# for y in l:
#     print(y)
#
# for x in i:
#     print(x)
#
# i = iter(l)
#
# for x in i:
#     print(x)
#endregion

class NumIterator(object):
    def __new__(cls, start, end):
        assert isinstance(start, int) and isinstance(end, int), "Both start and end must be integers"
        assert start <= end, "Start must be less than or equal to end"
        return super().__new__(cls)

    def __init__(self, start, end):
        self.start = start
        self.end = end + 1

    def __iter__(self):
        x = self.start
        while x < self.end:
            yield x
            x += 1

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            x = self.start
            self.start += 1
            return x

num_iter = NumIterator(1, 10)

for x in num_iter:
    print(x)

try:
    while next(num_iter):
        print("Anurag")
except StopIteration:
    print("Done")
