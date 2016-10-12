"""
Binary search Lab wiritten by Kevin Oyowe
October 12, 2016
"""
class BinarySearch(list):
    def __init__(self, a, b):
        super(self.__class__, self).__init__(range(a))
        self.length = a
        self.step = b
 
    def __getitem__(self, index):
        return (index + 1) * self.step
 
    def search(self, item):
 
        first = 0
        last = self.length - 1
        found = False
 
        index = -1
        count = 0
 
        while first <= last and not found:
            midpoint = (first + last) / 2
            if self.__getitem__(midpoint) == item:
                found = True
                index = midpoint
            else:
                if item < self.__getitem__(midpoint):
                    last = midpoint - 1
                else:
                    first = midpoint + 1
            count += 1
 
        return {"index": index, "count": count}