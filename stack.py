
class Node:
    """
    An inner class to hold a value and a next reference for the linked list.
    """
        
    def __init__(self,value) :
        self.value = value
        self.next = None;

class stack:
    """
    An implementation of the linked-list-stack data structure.
    """

    def __init__(self) :
        """
        Default constructor.
        """

        self.root = None
        self.length = 0

    def add(self,value):
        """
        Adds an item to the top of the stack.
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
        Removes and returns the top element of the stack.
        """

        pop = self.root
        self.root = pop.next
        self.length -= 1

        return pop.value
    

    def popAll(self):
        returnlist = []
        
        returnlist.append(self.root.value)
        self.root = self.root.next

        while(self.root != None):

            returnlist.append(self.root.value)

            self.root = self.root.next
            self.length -= 1

        return returnlist

        
    # Returns a string that can be printed
    def printString(self):
        """
        Returns a string of the entire stack to be printed into the console.
        """
        currentNode = self.root
        printString = ""
        while(currentNode.next != None):
            printString += str(currentNode.value)+"|"
            currentNode = currentNode.next
        printString += str(currentNode.value)

        return printString

list = stack()
list.add(10)
list.add(5)
list.add(3)
list.add(3)
list.add(3)
list.add(1)
list.add(2)
list.add(4)

print(list.printString())

print(list.pop())

print(list.printString())

print(list.popAll())
