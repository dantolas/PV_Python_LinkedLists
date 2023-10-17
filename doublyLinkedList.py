
class Node:
    """
    An inner class to hold a value, and the next/prev reference for the linked list.
    """
        
    def __init__(self,value) :
        self.value = value
        self.next = None
        self.prev = None

class linkedList:
    """
    An implementation of the doubly-linked-list data structure.
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
        Adds an item to the list.
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
        Removes the last element of the list.
        """
        self.tail = self.tail.prev
        self.root.prev = self.tail
        self.tail.next = self.root
        self.length -= 1

    
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

        
    # Returns a string that can be printed
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

list = linkedList()
list.add(10)
list.add(5)
list.add(3)
list.add(5)
list.add(5)
list.add(5)
list.add(4)
list.add(2)

print("List length:"+str(list.length))

print("List root:"+str(list.root.value))

print("List tail:"+str(list.tail.value))

print("root - next:"+str(list.root.next.value))

print("root - prev:"+str(list.root.prev.value))

print("List printed:"+list.printString())

print(list.get(2))

list.pop()

print(list.printString())


