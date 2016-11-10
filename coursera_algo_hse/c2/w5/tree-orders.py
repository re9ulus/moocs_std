# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrderRec(self, key):
    if key == -1:
      return
    else:
      self.inOrderRec(self.left[key])
      self.result.append(self.key[key])
      self.inOrderRec(self.right[key])

  def preOrderRec(self, key):
    if key == -1:
      return
    else:
      self.result.append(self.key[key])
      self.preOrderRec(self.left[key])
      self.preOrderRec(self.right[key])

  def postOrderRec(self, key):
    if key == -1:
      return
    else:
      self.postOrderRec(self.left[key])
      self.postOrderRec(self.right[key])
      self.result.append(self.key[key])

  def inOrder(self):
    self.result = []
    self.inOrderRec(0)        
    return self.result

  def preOrder(self):
    self.result = []
    self.preOrderRec(0)        
    return self.result

  def postOrder(self):
    self.result = []
    self.postOrderRec(0)         
    return self.result

def main():
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

# main()