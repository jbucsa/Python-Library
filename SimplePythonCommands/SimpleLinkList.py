class Node:
    def __init__(self, data, data2, reference='null', reference2='null', TFStatement= True):
        self.data = data
        self.data2 = data2
        self.reference = reference
        self.reference2 = reference2
        self.TFStatement = TFStatement 


# node1 = Node(1,10,3, 4,  False)
# print(node1.data)
# print(node1.reference2)
# print(node1.TFStatement)
# node1.TFStatement = True
# print(node1.TFStatement)

# node2 = Node(11)
# node1.reference = node2
# print(node1.reference)

class NodeStarter:
  def __init__(self, data, reference=None):
    self.data = data
    self.reference = reference

# class NewNode:
    def __init__(self, newData, newReference=None):
        self.newData = newData


class LinkedList: 
    def __init__(self, head=None,):
        self.head = head
    
    def add_to_start(self, data):
        n_node = NodeStarter(data)
        n_node.reference = self.head
        self.head = n_node

  
    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference
    
    # def add_item(self, new_data):
        # new_node = Node(new_data)
        # if self.head is None:
            # self.head = new_node
            # return
        # last = self.head
        # while last is not None:
            # last = last.reference
            # last = new_node





LinkedList1 = LinkedList()
LinkedList1.print_linked_list()

linked_list1 = LinkedList()
linked_list1.print_linked_list()
linked_list1.add_to_start(82)
linked_list1.print_linked_list()

linked_list1.add_to_start(15)
linked_list1.print_linked_list()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()
# linked_list1.add_item(15)
print(linked_list1)