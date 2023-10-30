class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 3 variant
max_counter = 0


def max_binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0
    global max_counter
    left_height = 0
    right_height = 0
    current_node = tree
    while current_node.left is not None:
        left_height += 1
        current_node = current_node.left
    current_node = tree
    while current_node.right is not None:
        right_height += 1
        current_node = current_node.right
    counter = left_height + right_height
    if counter > max_counter:
        max_counter = counter
    max_binary_tree_diameter(tree.left)
    max_binary_tree_diameter(tree.right)
    return max_counter

def max_binary_tree_diameter(tree):
    if tree is None:
        return 0

    max_diameter = 0
    stack = [tree]

    while stack:
        current_node = stack.pop()

        left_height = 0
        left_node = current_node
        while left_node.left:
            left_height += 1
            left_node = left_node.left

        right_height = 0
        right_node = current_node
        while right_node.right:
            right_height += 1
            right_node = right_node.right

        max_diameter = max(max_diameter, left_height + right_height)

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)

    return max_diameter


def binary_tree_diameter(tree: BinaryTree, left_node: BinaryTree, right_node: BinaryTree) -> int:
    if tree is None:
        return 0

    stack = [tree]

    while stack:
        current_node = stack.pop()

        left_height = 0
        current_left_node = current_node
        while current_left_node.left:
            left_height += 1
            current_left_node = current_left_node.left

        right_height = 0
        current_right_node = current_node
        while current_right_node.right:
            right_height += 1
            current_right_node = current_right_node.right

        if current_right_node is right_node and current_left_node is left_node:
            return right_height + left_height

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)


root = BinaryTree(1)
right = root.right = BinaryTree(2)
root.left = BinaryTree(3)
root.left.right = BinaryTree(4)
root.left.left = BinaryTree(7)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
left = root.left.right.right.right.right = BinaryTree(12)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)

print(max_binary_tree_diameter(root))
print(binary_tree_diameter(root, left, right))
