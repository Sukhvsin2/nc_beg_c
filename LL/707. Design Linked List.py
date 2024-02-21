class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        temp = self.left.next
        while temp and index > 0:
            temp = temp.next
            index -= 1
        
        if temp and temp != self.right and index == 0:
            return temp.data
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.prev = self.left
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -=1

        if curr and index == 0:
            node = Node(val)
            node.next = curr
            node.prev = curr.prev
            curr.prev.next = node
            curr.prev = node        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -=1
        
        if curr and curr != self.right and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
