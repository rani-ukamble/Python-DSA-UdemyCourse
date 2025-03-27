class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        if self.size()==0:
            return None
        else:
            temp = self.peek()
            self.stack_list.pop()
            return temp


def is_balanced_parentheses(str):
    new_stack = Stack()
    for i in str:
        if i=='[' or i=='{' or i=='(':
            new_stack.push(i)
        elif (i==')' and new_stack.peek()=='(') or (i==']' and new_stack.peek()=='[') or (i=='}' and new_stack.peek()=='{'):
            new_stack.pop()
        else:
            new_stack.push(i)
    if new_stack.is_empty():
        return True
    return False 
            
def reverse_string(str):
    my_stack = Stack()
    ans = ""
    for char in str:
        my_stack.push(char)
    while my_stack.size()!=0:
        top = my_stack.peek()
        ans+=top
        my_stack.pop()
    return ans


def sort_stack(ip_stack):
    sorted_stack = Stack()
    while ip_stack.size()!=0:
        temp = ip_stack.peek()
        ip_stack.pop()
        
        while sorted_stack.size()!=0 and sorted_stack.peek()>temp:
            x = sorted_stack.peek()
            sorted_stack.pop()
            ip_stack.push(x)
        sorted_stack.push(temp)
    while sorted_stack.size()!=0:
        y = sorted_stack.peek()
        ip_stack.push(y)
        sorted_stack.pop()


            
my_stack = Stack()
my_stack.push(5)
my_stack.push(2)
my_stack.push(8)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1
    
    Popped node:
    3
    
    Stack after pop():
    2
    1
 
"""

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

