class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
        
    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
    def find_min(self):
            if self.left:
                return self.left.find_min()
            else:
                return self.data     
    def find_max(self):
            if self.right:
                return self.right.find_max()
            else:
                return self.data   
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements   
           
    def calculate_sum(self):
        sum = 0
        elements = self.in_order_traversal()
        for i in elements:
            sum += i
        return sum 
       
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        return elements 

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
            

        return elements       
         
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)            
        return self     

def build_tree(elements):
    if not elements:
        return None
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

    
    # ------------------------------------------------------------EXERCISE----------------------------------------------------------------------------
#     1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree


if __name__ == '__main__':
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(elements)
    print(tree.find_max())
    print(tree.find_min())
    print(tree.in_order_traversal()) 
    print(tree.calculate_sum())  
    tree.delete(20)
    print(tree.in_order_traversal()) 