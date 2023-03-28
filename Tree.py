class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class GenNode:
    def __init__(self, data, child=[]):
        self.data = data
        self.child = child




class Tree:
    """      A
        B  C  D  E
      F,G  H I,J  K,L,M
    """
    def create_tree(self):
        return GenNode('A',
                       [GenNode('B', [GenNode('F'), GenNode('G')]),
                        GenNode('C', [GenNode('H')]),
                        GenNode('D', [GenNode('I'), GenNode('J')]),
                        GenNode('E', [GenNode('K'), GenNode('L'), GenNode('M')])]
                       )
    def level_order_traversal(self, root):
        if root is None: return
        x = [root]
        while x:
            node = x.pop(0)
            print(node.data)
            if node.child: x += node.child

    def pre_order_traversal(self, root):
        #  FBG A
        if root == None: return
        print(root.data)
        for i in root.child:
            self.pre_order_traversal(i)
    def inorder_firstparent(self, node):

        # Parent before second last child
        if node == None: return
        for i in node.child[:-1]:
            self.inorder_firstparent(i)
        print(node.data, end=', ')
        if node.child: self.inorder_firstparent(node.child[-1])

    def inorder_lastparent(self, node):

        # Parent after first child
        if node == None: return
        if node.child: self.inorder_lastparent(node.child[0])
        print(node.data, end=', ')
        for i in node.child[1:]: self.inorder_lastparent(i)

    def post_trs(self, root):
        def post_order_traversal(root):
            if root == None: return
            for i in root.child:
                post_order_traversal(i)
                print(i.data)

        post_order_traversal(root)
        print(root.data)



class BinaryTree:
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
            



tree1 = BinaryTree()
tree = Tree()
x = tree.create_tree()
y = tree1.create_tree()

# print('in-order traversal')
# tree.inorder_firstparent(x)
#
# print('in-order traversal')
# tree1.in_order_traversal(y)

# print('\n pre-order traversal')
# tree.pre_order_traversal(x)
#
# print('\n pre-order traversal1')
# tree1.pre_order_traversal(y)

# print('\n post-order traversal')
# tree.post_trs(x)
#
# print('\n post-order traversal')
# tree1.post_order_traversal(y)
#
print('\n level order traversal')
tree.level_order_traversal(x)