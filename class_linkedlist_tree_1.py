class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right, self.left = None, None

    def add(self, value):
        if not value == self.val:
            if value > self.val:
                if not self.right:
                    self.right = TreeNode(value)
                else:
                    self.right.add(value)
            elif value < self.val:
                if not self.left:
                    self.left = TreeNode(value)
                else:
                    self.left.add(value)
            else:
                raise ValueError("Value exists.")
        else:
            raise ValueError("Value exists.")
    
    def find(self, value):
        if self.val == value:
            return True
        elif value > self.val:
            if not self.right: 
                raise Exception("No such value.")
            self.right.find(value)
        elif value < self.val:
            if not self.left:
                raise Exception("No such value.")
            self.left.find(value)

def levelOrder(root):
    if not root:
        return []
    
    queue = [root]
    results = []
    while queue:
        next_queue = []
        results.append([node.val for node in queue])
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return results