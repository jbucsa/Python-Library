#Part 1: Create a BSTNode class
class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)

#Part 2: Create a BST class
class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []
  
  def __str__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def __repr__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)  

  #Part 3: Add functionality to your BST class
  def add(self,node):
    #data wrong type
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must pass an int or a BSTNode")

    #data int, make new BSTNode
    if type(node) == int:
      node = BSTNode(node)

    #node already in tree
    if node.data in self.contents:
      return

    #tree empty
    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

    #call new (recursive) function; don't need to check other conditions again
    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    # New node bigger - go right
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        #recurse/traverse
        self.add_node(cur_node.right, new_node)
    else: #new node smaller, go left
      if cur_node.left == None:
        cur_node.left = new_node
        self.contents.append(new_node.data)
        return
      else:
        #recurse/traverse
        self.add_node(cur_node.left, new_node)
  
  # bonus content
  def remove(self, node):
    #data wrong type
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("You must pass an int or a BSTNode")

    #data BSTNode, make int
    if type(node) == BSTNode:
      node = node.data

    #node already in tree
    if node not in self.contents:
      raise ValueError("Value not in tree")

    #call new (recursive) function; don't need to check other conditions again
    self.remove_node(self.root, node)

  def remove_node(self, cur_node, rem_node, prev_node = None):
    # found node, now remove
    if rem_node == cur_node.data:
      #rem_node has no children
      if cur_node.right == None and cur_node.left == None:
        if cur_node == prev_node.right:
          prev_node.right = None
          self.contents.remove(rem_node)
        else:
          prev_node.left = None
          self.contents.remove(rem_node)
      #rem_node has one child
      elif cur_node.right == None and cur_node.left != None:
        if cur_node == prev_node.right:
          prev_node.right = cur_node.left
          self.contents.remove(rem_node)
        else:
          prev_node.left = cur_node.left
          self.contents.remove(rem_node)
      elif cur_node.left == None and cur_node.right != None:
        if cur_node == prev_node.left:
          prev_node.left = cur_node.right
          self.contents.remove(rem_node)
        else:
          prev_node.right = cur_node.right
          self.contents.remove(rem_node)
      #rem_node has two children
      else:
        self.nodes = []
        self.traverse_tree(cur_node) #get list of all descendants
        self.nodes.remove(rem_node) #remove node we're removing from list
        self.contents.remove(rem_node)
        # remove node and all descendants
        if cur_node == prev_node.right:
          prev_node.right = None
        else:
          prev_node.left = None
        # add all descendants back into tree
        for node in self.nodes:
          self.add(node)
    #wrong node, traverse
    elif rem_node > cur_node.data:
      self.remove_node(cur_node.right, rem_node, prev_node = cur_node)
    elif rem_node < cur_node.data:
      self.remove_node(cur_node.left, rem_node, prev_node = cur_node)
      
  def traverse_tree(self, node):
    if node != None:
      self.traverse_tree(node.right)
      self.nodes.append(node.data)
      self.traverse_tree(node.left)


#test code
node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5

bst = BST()
print(bst) #The tree is empty

print('=======================\n')

bst.root = node2
print(bst)
#output:
# -> 4
#     -> 3

print('=======================\n')

node2.right = node3
print(bst)
#output:
#     -> 5
# -> 4
#     -> 3

#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)

print('=======================\n')
print(bst)
# output:
#         -> 14
#             -> 13
#     -> 10
# -> 8
#             -> 7
#         -> 6
#             -> 4
#     -> 3
#         -> 1

print('=======================\n')
bst.remove(1) #leaf/end node
print(bst)
# output:
#         -> 14
#             -> 13
#     -> 10
# -> 8
#             -> 7
#         -> 6
#             -> 4
#     -> 3

print('=======================\n')
bst.remove(10) #middle node
print(bst)
# output:
#     -> 14
#         -> 13
# -> 8
#             -> 7
#         -> 6
#             -> 4
#     -> 3

