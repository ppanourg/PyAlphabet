import sys
from collections import deque
from heapq import heappush, heappop

class Node:
  """A 'private' node class for the dictionary to play with"""

  def __init__(self, word="", freq=0, parent=None, is_key=False, sub_tree_freq=0):
    """Initialiser"""
    #This is a python built-in dictionary, not a dictionary like what we are going
    #to implement... more like a hash map.
    self.map           = {}

    self.word          = word
    self.freq          = freq
    self.parent        = parent
    self.is_key        = is_key
    self.sub_tree_freq = sub_tree_freq

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
##*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

class Dictionary:
  """A Dictionary w/ a multiway trie backend"""

  def __init__(self):
    self.root = Node()

  def insert(self, word, frequency):
    iter = self.root
    index = 0

    while index < len(word):
      symbol = word[index]

      if word[index] in iter.map:
        iter = iter.map[symbol]
      else:
        iter.map[symbol] = Node()
        iter.map[symbol].parent = iter
        iter = iter.map[symbol]

      index = index + 1

    if iter.is_key == True:
      return False
    else:
      iter.word = word
      iter.freq = frequency
      iter.is_key = True

      #Updating the sub_tree_freq for all nodes in a direct path up to the root
      while iter != None:
        iter.sub_tree_freq += frequency
        iter = iter.parent

      return True

  def find(self, word, node=None, return_prefix_node=False):
    if node == None: node = self.root 
    if len(word) == 0:
      if return_prefix_node == False:
        return node.is_key
      else:
        return node

    if word[0] in node.map:
      return self.find(word[1:len(word)], node.map[word[0]], return_prefix_node)
    else:
      return False

  def predict(self, prefix, num):
    #Get a reference to the node at the end of the prefix.
    prefix_node = self.find(prefix, self.root, return_prefix_node=True)

    #If that prefix does not exit just return an empty list.
    if prefix_node == False or num <= 0: return []
    
    #Create a queue for BFS and a heap for optimizing the search.
    heap = []
    queue = deque([prefix_node])

    while len(queue) > 0:
      curr = queue.popleft()

      for symbol in curr.map:
        node = curr.map.get(symbol)
        if len(heap) >= num and node.sub_tree_freq < heap[0][0]: continue
        queue.append(node)

      if curr.is_key:
        if len(heap) < num:
          heappush(heap, (curr.freq, curr))
        elif curr.freq > heap[0][0]:
          heappop(heap)
          heappush(heap, (curr.freq, curr))

    ret = []
    while len(heap) > 0: ret.insert(0, heappop(heap)[1].word)

    return ret
       
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
##*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

class LoadDict:
  """A Helper class for loading a dictionary"""

  @staticmethod
  def load(filename=sys.argv[1]):
    file = open(filename,'r')
    dict = Dictionary()
    for line in file:
      i = 0
      temp = ""
      while True:
        if line[i] >= '0' and line[i] <= '9': 
          temp = temp + str(line[i])
          i = i + 1
        else: 
          dict.insert(line[i + 1:len(line) - 1], int(temp))
          break

    return dict


