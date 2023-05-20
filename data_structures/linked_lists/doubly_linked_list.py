class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.pev=None
class LinkedList():
    def __init__(self):
        self.head=None
    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=Node(value)
            current_node.next.pev=current_node
    def show_element(self):
        current_node=self.head
        while  current_node is not None:
            print(current_node.data)
            current_node=current_node.next
    def get_element(self, position):
        i = 0
        current_node = self.head
        while current_node is not None:
            if i == position:
                return current_node.data
            current_node = current_node.next
            i += 1
        return None
    def delete(self,position):
        if position==0:
            current_node=self.head
            self.head=self.head.next
            self.head.prv=None
            return current_node.data
        else:
            current_node=self.head
            for i in range(0,position):
                p=current_node
                current_node=current_node.next
            p.next=current_node.next
            if current_node.next is  not None:
                current_node.next.prv=p

            return current_node.data        
'''
test case:
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.show_element()
1
3
5
list1.delete(1)
list1.show_element()
1
5
'''  