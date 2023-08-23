class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if self.data == data:
            return
        
        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, data):
        if self.data == data:
            return True
        if self.data > data:
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

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum += self.right.calculate_sum()
        return sum
                

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements


if __name__ == '__main__':
    root = BinarySearchTree(17)
    nums = [12, 2, 3, 33, 45, 55, 17, 20, 19, 44]
    for n in nums:
        root.add_child(n)
    print(f"In Order Traversal: {root.in_order_traversal()}")
    print(f"Post Order Traversal: {root.post_order_traversal()}")
    print(f"Pre Order Traversal: {root.pre_order_traversal()}")
    print(f"Minimum element in Entire Tree: {root.find_min()}")
    print(f"Maximum element in Entire Tree: {root.find_max()}")
    print(f"sum of the all element in the Tree: {root.calculate_sum()}")
    print(f"Is 20 exist in Tree: {root.search(20)}")
    print(f"Is 89 exist in Tree: {root.search(89)}")

