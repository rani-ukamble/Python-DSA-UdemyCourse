class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == value:
                return False
            if value<temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right =  new_node
                    return True
                temp = temp.right

                

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
            
    def BFS(self):
        current_node = self.root 
        queue = []
        results = [] 
        queue.append(current_node) 

        while len(queue)>0:
            current_node = queue.pop(0) 
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def preOrder(self, node = None, res = None):
        if res == None:
            res = []
        if node == None:
            node = self.root
        res.append(node.value)
        if node.left:
            self.preOrder(node.left, res)
        if node.right:
            self.preOrder(node.right, res) 
        return res 

    def preOrder1(self):
        res = []

        def traverse(current_node):
            res.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return res
    
    def postOrder(self):
        res = [] 

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            res.append(current_node.value)  

        traverse(self.root)
        return res
    
    def inOrder(self):
        res = [] 

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            res.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)  

        traverse(self.root)
        return res 
    
    



    


mytree = BinarySearchTree()
# print(mytree.root)
mytree.insert(47)
mytree.insert(21)
mytree.insert(76)
mytree.insert(18)
mytree.insert(27)
mytree.insert(52)
mytree.insert(82)



# print(mytree.BFS())

# [47, 21, 76, 18, 27, 52, 82]

print(mytree.inOrder())
