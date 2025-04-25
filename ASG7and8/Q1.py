#Write a Python program to create a class representing a linked list data structure. Include
#methods for displaying linked list data, inserting and deleting nodes.

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    class node:
        def __init__(self,data:int):
            self.data = data
            self.next = None

    # head:node = None
    # size = 0

    def insert(self,index,data):
        newNode = self.node(data)
        if(self.head is None):
            self.head = newNode
            self.size += 1
            return
        
        elif(index == 0):
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return
        
        temp = self.head
        for i in range(index-1):
            temp = temp.next

        if(index != self.size):
            newNode.next = temp.next
        temp.next = newNode
        self.size += 1


    def delete(self,index)->int:
        if(self.head is None):
            print("Linked list is empty . Nothing to delete.")
            return -1
        elif(index == 0):
            data = (self.head).data
            self.head = (self.head).next
            self.size -= 1
            return data
        
        temp = self.head

        for i in range(index-1):
            temp = temp.next
            if(temp is None):
                return -1
    
        data = temp.next.data

        if(index == self.size-1):
            temp.next = None
            self.size -= 1
            return data
        else:
            temp.next = temp.next.next
            self.size -= 1
            return data

    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next


l1 = LinkedList()
l1.insert(0,12)
l1.insert(1,34)
l1.insert(2,45)
l1.insert(3,56)
l1.insert(4,67)
print(l1.delete(2))
print("")

l1.display()