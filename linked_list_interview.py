class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def partition_list(self, x):
        curr = self.head 
        dummy1 = Node(0) 
        dummy2 = Node(0) 
        
        temp1 = dummy1 
        temp2 = dummy2 
        
        while curr is not None:
            if curr.value<x:
                temp1.next = curr 
                temp1 = temp1.next 
            else:
                temp2.next = curr 
                temp2 = temp2.next 
            curr = curr.next
        temp2.next = None
        temp1.next = dummy2.next 
        self.head = dummy1.next 
        
        return self.head

    def remove_duplicates(self):
        if not self.head:
            return None
        l = []
        first = self.head 
        l.append(first.value)
        second = first.next 
        while first.next is not None:
            if second.value in l:
                first.next = second.next 
                second = first.next
            else:
                l.append(second.value)
                second = second.next 
                first = first.next 
        return self.head

    def binary_to_decimal(self):
        l = 0
        temp = self.head
        while temp:
            l+=1 
            temp = temp.next 
        sum = 0 
        temp = self.head
        while temp:
            sum += (temp.value * 2**(l-1)) 
            l-=1 
            temp = temp.next
        return sum


    def reverse_between(self, start, end):
        if self.head==None or self.head.next == None:
            return None
        t = 0 
        temp = self.head
        l = []
        while temp:
            if t in range(start, end+1):
                l.append(temp.value)
            temp = temp.next
            t+=1 
        t = 0 
        temp = self.head
        while temp:
            if t in range(start, end+1):
                temp.value = l.pop()
            temp = temp.next
            t+=1
        return self.head 
    
    def swap_pairs(self):
        if not self.head or not self.head.next:
            return None
        dummy = Node(0)
        dummy.next = self.head 
        prev = dummy
        curr  = self.head 
        
        while curr and curr.next :
            first = curr 
            second = curr.next
            
            # swapping
            prev.next = second
            first.next = second.next 
            second.next = first
            
            # update prev and curr 
            prev = first 
            curr = first.next
            
        self.head = dummy.next
            
        return self.head

    

ll = LinkedList(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(5)
ll.print_list() # type: ignore