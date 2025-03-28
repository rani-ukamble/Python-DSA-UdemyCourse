class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    
    def merge(self, l2):
        dummy = Node(0) 
        curr = dummy
        
        l1_curr = self.head 
        l2_curr = l2.head 
        
        while l1_curr is not None and l2_curr is not None:
            if l1_curr.value < l2_curr.value:
                curr.next = l1_curr 
                l1_curr = l1_curr.next 
            else:
                curr.next = l2_curr 
                l2_curr = l2_curr.next 
            curr = curr.next 
            
        while l1_curr is not None:
            curr.next = l1_curr 
            l1_curr = l1_curr.next
            curr = curr.next
        while l2_curr is not None:
            curr.next = l2_curr 
            l2_curr = l2_curr.next 
            curr = curr.next
        
        self.head = dummy.next 
        
        # return self.head
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""