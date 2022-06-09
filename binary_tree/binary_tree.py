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
