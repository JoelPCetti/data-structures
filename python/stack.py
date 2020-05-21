class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    return self.stack.pop()

  def size(self):
    return len(self.stack)


