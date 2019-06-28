class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #append an element by overwriting the old one.
    self.storage[self.current] = item
    self.current = (self.current + 1) % self.capacity

  def get(self):
    #return a list of elements from the oldest to the newest
    ring = [x for x in self.storage if x is not None]
    return ring