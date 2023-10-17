
class Node:
    """
    An inner class to hold a value and a next reference for the linked list.
    """
        
    def __init__(self,value) :
        self.value = value
        self.next = None;

class linkedList:
    """
    An implementation of the linked-list data structure.
    """

    def __init__(self) :
        """
        Default constructor.
        """

        self.root = None
        self.length = 0

    def add(self,value):
        """
        Adds an item to the list.
        """
        self.length += 1

        node = Node(value)        

        if(self.root is None):
            self.root = node
            self.root.next = None 
            return
        
        
        node.next = self.root
        self.root = node


    def pop(self):
        """
        Removes and returns the first element of the list.
        """

        pop = self.root
        self.root = pop.next

        return pop

    
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
        currentNode = self.root
        printString = ""
        while(currentNode.next != None):
            printString += str(currentNode.value)+"|"
            currentNode = currentNode.next
        printString += str(currentNode.value)

        return printString

list = linkedList()
list.add(10)
list.add(5)
list.add(3)

print("List length:"+str(list.length))

print("List root:"+str(list.root.value))

print("List tail:"+str(list.tail.value))

print("root - Next:"+str(list.root.next.value))

print("List printed:"+list.printString())

print(list.get(2))

list.pop()

print(list.printString())


