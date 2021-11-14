#Linked list Example 


# the node class
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

    def getData(self):
        return self.val
    
    def set_data(self,val):
       self.val = val

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next


# the linkedList class

class LinkedList(object):
    def __init__(self,head = None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count+=1

    def find(self,val):
        item = self.head
        while item != None:
            if item.getData() == val:
                return item
            item = item.next
        return None

    def delete(self,idx):
        # delete an item in a given index
        if idx < self.count-1:
            if idx == 0:
                self.head = self.head.next
            else:
                tmp = 0
                node = self.head
                while tmp < idx-1:
                    node = node.get_next()
                    tmp +=1
                node.set_next(node.get_next().get_next())
                self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node :",tempnode.getData())
            tempnode = tempnode.get_next()


#create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(10)
itemlist.insert(12)
itemlist.insert(32)
itemlist.insert(11)
itemlist.insert(9)
itemlist.dump_list()

#exercise the list 
# print("Item count :",itemlist.count)
# print("Finding item :",itemlist.find(13))
# print("Finding item :",itemlist.find(9))

#delete item on list
itemlist.delete(0)
itemlist.delete(0)
print("aftere deletion :=)")
itemlist.dump_list()

