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
        
    
    def bubble_sort(self):
        if self.head is None:
            return None
        
        temp = self.head    
        cnt = 0
        while temp is not None:
            cnt+=1 
            temp = temp.next 
            
        for i in range(cnt-1):
            temp = self.head 
            for j in range(cnt-1-i):
                first = temp
                second = first.next
                if first.value>second.value:
                    first.value, second.value = second.value, first.value 
                temp = temp.next 
      
        
    def selection_sort(self):
        if self.head is None:
            return None
            
        temp = self.head
        cnt = 0
        while temp is not None:
            cnt += 1
            temp = temp.next
            
        for i in range(cnt-1):
            temp = self.head
            
            for _ in range(i):
                temp = temp.next
                
            mini_node = temp
            curr_node = temp.next 
            
            while curr_node is not None:
                if curr_node.value < mini_node.value:
                    mini_node = curr_node
                curr_node = curr_node.next
                
            if temp.value > mini_node.value:
                temp.value, mini_node.value = mini_node.value, temp.value        

   
    def insertion_sort(self):
        if self.head==None or self.head.next==None:
            return
        dummy = Node(0)
        dummy.next = self.head 
        prev, curr = self.head, self.head.next 
        
        while curr:
            if curr.value>=prev.value:
                prev, curr = curr, curr.next
                continue 
            
            temp = dummy 
            while curr.value>temp.next.value:
                temp = temp.next
                
            prev.next = curr.next 
            curr.next = temp.next 
            temp.next = curr 
            curr = prev.next
            
        self.head = dummy.next
        
        return self.head
            


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

