# python2

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.size = 0

  def ReadData(self):
    n = int(raw_input())
    self._data = [0] + [int(s) for s in raw_input().split()]
    self.size = n
    assert n == len(self._data) - 1

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print('{0} {1}'.format(swap[0], swap[1]))

  @staticmethod
  def Parent(i):
    return i / 2

  @staticmethod
  def LeftChild(i):
    return i * 2

  @staticmethod
  def RightChild(i):
    return i * 2 + 1

  def SiftDown(self, i):
    maxIndex = i
    left, right = self.LeftChild(i), self.RightChild(i)
    if left <= self.size and self._data[left] < self._data[maxIndex]:
      maxIndex = left
    if right <= self.size and self._data[right] < self._data[maxIndex]:
      maxIndex = right
    if i != maxIndex:
      self._swaps.append((i-1, maxIndex-1))
      self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]
      self.SiftDown(maxIndex)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]
    for i in reversed(range(1, len(self._data)/2+1)):
      self.SiftDown(i)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
