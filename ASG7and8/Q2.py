# Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    

    def enqueue(self,data:int):
        newNode = self.Node(data)
        if(self.__front is None):
            self.__front = newNode
            self.__rear = newNode
            return
        self.__rear.next = newNode
        self.__rear = newNode
        return
    
    def dequeue(self):
        if(self.__front is None and self.__rear is None):
            print("Queue is empty . So dequeue cam't be done.")
            return -1
        elif(self.__front == self.__rear):
            data = self.__front.data
            self.__front = None
            self.__rear = None
            return data
        
        data = self.__front.data
        self.__front = self.__front.next
        return data
    
    def display(self):
        temp = self.__front
        while(temp is not None):
            print(temp.data,end="->")
            temp = temp.next
    

q1 = Queue()
q1.enqueue(12)
q1.enqueue(34)
q1.enqueue(23)
q1.enqueue(45)
q1.enqueue(67)
print(q1.dequeue())
print(q1.dequeue())
print("")
q1.display()