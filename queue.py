
class Node:
    """
    An inner class to hold a value, and the next/prev reference for the linked list.
    """
        
    def __init__(self,value) :
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    """
    An implementation of the queue data structure.
    """

    def __init__(self) :
        """
        Default constructor.
        """

        self.root = None
        self.tail = None
        self.length = 0

    def add(self,value):
        """
        Adds an item to the end of the list.
        """
        self.length += 1

        node = Node(value)        

        if(self.root is None):
            self.root = node
            self.tail = node
            self.root.next = self.tail
            self.root.prev = self.tail
            self.tail.prev = self.root
            self.tail.next = self.root
            return
        
        self.tail.next = node
        self.root.prev = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = self.root


    def pop(self):
        """
        Removes the first element of the list.
        """

        if(self.length <= 0):
            raise Exception("Cannot pop empty queue");

        returnNode = self.root

        self.root = self.root.next
        self.tail.next = self.root
        self.root.prev = self.tail
     
        self.length -= 1
        return returnNode.value


    
    def remove(self,index):
        """
        Removes element at index.
        """
        if(index >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(index):
            prevNode = currentNode
            currentNode = currentNode.next
            
        prevNode.next = currentNode.next
        self.length -= 1
        del currentNode

        
    
    def get(self,index):
        """
        Returns element at index.
        """
        if(index >= self.length):
            raise Exception("Index out of bounds exception")
        
        currentNode = self.root

        for i in range(index):
            currentNode = currentNode.next
        return currentNode.value

        
    def printString(self):
        """
        Returns a string of the entire list to be printed into the console.
        """
        currentNode = self.root.next
        printString = str(self.root.value)+"|"
        while(currentNode != self.root):
            printString += str(currentNode.value)+"|"
            currentNode = currentNode.next


        return printString


    def popAll(self):
        returnlist = []
        
        returnlist.append(self.root.value)
        currentNode = self.root.next

        while(currentNode != self.root):
            returnlist.append(currentNode.value)
            currentNode.prev = None
            currentNode = currentNode.next

        return returnlist


queue = Queue()
queue.add(10)
queue.add(5)
queue.add(3)
queue.add(5)
queue.add(5)
queue.add(5)
queue.add(4)
queue.add(2)

print("List length:"+str(queue.length))

print("List root:"+str(queue.root.value))

print("List tail:"+str(queue.tail.value))

print("root - next:"+str(queue.root.next.value))

print("root - prev:"+str(queue.root.prev.value))

print("List printed:"+queue.printString())

print(queue.get(2))

print(queue.pop())

print(queue.printString())

print(str(queue.popAll()))

