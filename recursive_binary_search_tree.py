class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            print(self.root.value)
            if self.root.left is not None:
                print(self.root.left.value)
            else:
                print("None")
            if self.root.right is not None:
                print(self.root.right.value)
            else:
                print("None")
        else:
            print("Tree is empty")


    def __r_contains(self, curr_node, value):
        if curr_node == None:
            return False
        if curr_node.value == value:
            return True
        if value < curr_node.value:
            return self.__r_contains(curr_node.left, value)
        elif value > curr_node.value:
            return self.__r_contains(curr_node.right, value) 
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)




    def __r_insert(self, curr_node, value):
        if curr_node == None:
            return Node(value)
        if value < curr_node.value:
            curr_node.left = self.__r_insert(curr_node.left, value)
        elif value > curr_node.value:
            curr_node.right = self.__r_insert(curr_node.right, value)
        return curr_node
        
    def insert(self, value):
        if self.root==None:
            self.root = Node(value)
        self.__r_insert(self.root, value) 



    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left 
        return current_node.value 

    def __r_delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None 
            elif current_node.left == None:
                current_node = current_node.right 
            elif current_node.right == None:
                current_node = current_node.left 
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min 
                current_node.right = self.__r_delete_node(current_node.right, sub_tree_min)
        return current_node
            
    def delete_node(self, value):
        self.__r_delete_node(self.root, value)

    

    


mytree = BinarySearchTree()
# print(mytree.root)
mytree.insert(2)
mytree.insert(1)
mytree.insert(3)

print(mytree.root.value)
print(mytree.root.left.value)
print(mytree.root.right.value)

mytree.delete_node(2)

print("\n")
mytree.print_tree()

print('\nBST Contains 1:')
print(mytree.r_contains(1))