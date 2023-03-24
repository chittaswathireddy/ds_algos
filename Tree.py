class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    """
                A
             B       C
            D       E     F
                    G  H I
    """
    
    def create_tree(self):
        return Node('A', 
                    Node('B', Node('D'), None), 
                    Node('C', 
                        Node('E', None, Node('G')), 
                        Node('F', Node('H'), Node('I')))
                   )

    def in_order_traversal(self, root): 
        if root == None: return
        self.in_order_traversal(root.left)
        print(root.data)
        self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root==None: return
        print(root.data)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root==None: return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.data)

    def level_order_traversel(self, root):
        #bfs - stack
        x = [root]
        while x:
            node = x.pop(0)
            print(node.data)
            if node.left: x += [node.left]
            if node.right: x += [node.right]
            



tree = Tree()
x = tree.create_tree()
print('in-order traversal')
tree.in_order_traversal(x)
print('\n pre-order traversal')
tree.pre_order_traversal(x)
print('\n post-order traversal')
tree.post_order_traversal(x)

print('\n level order traversal')
tree.level_order_traversel(x)