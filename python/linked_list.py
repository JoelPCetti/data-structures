class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head = None):
    self.head = head
    self.next_node = None

  def add(self, data):
    current = self.head
    while current.next_node != None:
      current = current.next_node
    current.next_node = data
  
  def remove(self, data):
    if head.data == data:
      head = head.next
      return
    current = self.head 
    while current != None:
      if current.next_node.data == data:
        current.next_node = current.next_node.next_node
        return
      current = current.next_node

  def get(self, element_to_get):
    current = self.head
    counter = 0
    while current != None:
      if current == element_to_get:
        return counter
      counter+= 1

# ----- Node ------
class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None



        
      
    




