class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for item in ReverseListIterator([1, 2, 3, 4]):
    print(f'Reverse list iterator:{item}')

class EvenRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

for num in EvenRangeIterator(10):
    print(f'Even Range Iterator:{num}')
