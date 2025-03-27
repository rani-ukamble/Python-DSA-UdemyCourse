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
            

   
    
    # def make_empty(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head 
        while temp.next:
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp.value
    
    # insert at begin of llist
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if self.length == 0:
            return None 
        temp = self.head
        head = self.head.next 
        temp.next = None 
        self.length -= 1 
        if self.length == 0:
            self.tail = None 
        return temp.value 

    def get(self, index):
        if index<0 or index>=self.length:
            return None 
        temp = self.head
        for _ in range(index): 
            temp = temp.next 
        # return temp.value
        return temp

    def set(self, index, value):
        temp = self.get(index) 
        if temp:
            temp.value = value 
            return True
        return False

    def insert(self, index, value):
        if index<0 or index>self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value) 
        new_node = Node(value)
        temp = self.get(index-1) 
        new_node.next = temp.next 
        temp.next = new_node 
        self.length += 1 
        return True 
        
    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        if index==0: 
            self.popFirst()
        if index==self.length:
            self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None
        self.length -= 1
        return temp.value 


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp 
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow = slow.next 
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True 
        return False

def find_kth_from_end(self, k):
    fast = self.head
    slow = self.head 
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(4)
# print(my_linked_list.pop()) # 4
# print(my_linked_list.pop()) # 2
# my_linked_list.prepend(5)
# print(my_linked_list.popFirst())

my_linked_list.insert(3, 44)
# my_linked_list.tail.next = my_linked_list.head #for loop condition true



# print("********************\nList Elements: ")
# my_linked_list.print_list() 

# my_linked_list.reverse()

# print(f"Element at index 3 is: ", my_linked_list.get(3))
# print(my_linked_list.set(3, 33))

print("********************\nList Elements: ")
my_linked_list.print_list() #

print("************")
# print(my_linked_list.remove(3))

# print( my_linked_list.find_middle_node().value )
# print(my_linked_list.has_loop() ) # Returns False

# k = 2
# result = find_kth_from_end(my_linked_list, k)
# print(result.value)  # Output: 4




