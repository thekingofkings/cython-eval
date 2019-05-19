from collections import deque
from random import random
from time import time


class Node(object):
    """Node of a binary tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def preorder_traversal(cls, root, res):
        """Pre-order traversal of a tree at root node."""
        if root is None:
            return
        res.append(root.val)
        cls.preorder_traversal(root.left, res)
        cls.preorder_traversal(root.right, res)

    @classmethod
    def generate_random_tree(cls, num_nodes, threshold=0.8):
        """Generate a random binary tree with n nodes."""
        root = Node(0)
        cnt = 1
        queue = deque([root])
        while cnt < num_nodes and queue:
            cur = queue.popleft()
            if random() < threshold:
                left_child = Node(cnt)
                cur.left = left_child
                cnt += 1
                queue.append(left_child)
            if random() < threshold:
                right_child = Node(cnt)
                cur.right = right_child
                cnt += 1
                queue.append(right_child)
        return root

    @classmethod
    def pretty_print(cls, root, indent, last):
        """Pretty print a binary tree

        Keyword arguments:
        root -- root Node
        indent -- current indent as string
        last -- if the node is last child
        """
        if root is None:
            return
        print "{}{} {}".format(indent, "+-", root.val)
        indent += '   ' if last else '|  '
        left_is_last = root.right is None
        cls.pretty_print(root.left, indent, left_is_last)
        cls.pretty_print(root.right, indent, True)


def test_preorder_traversal(num_node=20000, threshold=0.8):
    """Test preorder traversal with randomly generated tree"""
    root = Node.generate_random_tree(num_node, threshold)
    preorder = []
    Node.preorder_traversal(root, preorder)


if __name__ == '__main__':
    NUM_TREES = 10
    BEGIN = time()
    for i in range(NUM_TREES):
        test_preorder_traversal(100000, 0.8)
    END = time()
    print "Tree generation/traversal speed {} seconds / tree".format(
        (END - BEGIN) / NUM_TREES)
