class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
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
    def show_element(self):
        current_node=self.head
        while  current_node is not None:
            print(current_node.data)
            current_node=current_node.next
    def lenght(self):
        current_node=self.head
        count=0
        while  current_node is not None:
            current_node=current_node.next
            count+=1
        return count
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
        pass

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.show_element()
print(list1.lenght())

