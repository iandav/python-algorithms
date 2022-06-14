from turtle import right


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# Creating the nodes
node0 = Node(3)
node1 = Node(4)
node2 = Node(5)

# Connecting the nodes
node0.left = node1
node0.right = node2

# Result:
#   (3)
#   | \
# (4) (5)

# Pointer to the root of the binary tree
tree = node0
print("tree result: Root value: {}, Left value: {}, Right value: {}".format(tree.value, tree.left.value, tree.right.value))

# Let's create another tree with more complexity using a tuple: (left_subtree, value, right_subtree)
# Where left_subtree and right_subtree are tuples too

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node

tree_2 = parse_tuple(tree_tuple)

# Result of tree_2:
#              (2)            Level 0
#              / \
#            (3) (5)___       Level 1
#            /   /     \
#          (1) (3)     (7)    Level 2
#                \     / \
#                (4) (6) (8)  Level 3

print(
    "tree_2 level 0 value: {}\ntree_2 level 1 values: {}, {}\ntree_2 level 2 values: {}, {}, {}\ntree_2 level 3 values: {}, {}, {}"
    .format(
        tree_2.value, # Level 0 values
        tree_2.left.value, tree_2.right.value, # Level 1 values
        tree_2.left.left.value, tree_2.right.left.value, tree_2.right.right.value, # Level 2 values
        tree_2.right.left.right.value, tree_2.right.right.left.value, tree_2.right.right.right.value # Level 3 values
    ))

# Tree traversals - Recursion is the way
# Creation of tree_3 to traverse it inorder, preorder and postorder
tree_3 = Node(2)
tree_3.left = Node(3)
tree_3.left.left = Node(1)
tree_3.right = Node(5)
tree_3.right.left = Node(3)
tree_3.right.left.right = Node(4)
tree_3.right.right = Node(7)
tree_3.right.right.left = Node(6)
tree_3.right.right.right = Node(8)

# Result of tree_3
#              (2)            
#              / \
#            (3) (5)___       
#            /   /     \
#          (1) (3)     (7)    
#                \     / \
#                (4) (6) (8) 

# Inorder Traversal [1, 3, 2, 3, 4, 5, 6, 7, 8]
# 1. Traverse the left subtree recursively inorder
# 2. Traverse the root
# 3. Traverse the right subtree recursively inorder

def inorder_traversal(node):
    if node is None:
        return []
    else:
        return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

print("Inorder traversal of tree_3:", inorder_traversal(tree_3))


# Preorder Traversal [2, 3, 1, 5, 3, 4, 7, 6, 8]
# 1. Traverse the root
# 2. Traverse the left subtree recursively preorder
# 3. Traverse the right subtree recursively preorder

def preorder_traversal(node):
    if node is None:
        return []
    else:
        return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)
    
print("Preorder traversal of tree_3:", preorder_traversal(tree_3))

# Postorder Traversal [1, 3, 4, 3, 6, 8, 7, 5, 2]
# 1. Traverse the left subtree recursively postorder
# 2. Traverse the root
# 3. Traverse the right subtree recursively postorder

def postorder_traversal(node):
    if node is None:
        return []
    else:
        return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]

print("Postorder traversal of tree_3:", postorder_traversal(tree_3))
