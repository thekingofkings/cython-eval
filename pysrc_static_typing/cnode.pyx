from collections import deque
from random import random


cdef class Node:
    """Node class of a binary tree"""
    cdef readonly int val
    cdef public Node left
    cdef public Node right

    def __init__(self, int val=0, Node left=None, Node right=None):
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
    def generate_random_tree(cls, int num_nodes, double threshold=0.8):
        """Generate a random binary tree with n nodes."""
        root = Node(0)
        cdef int cnt = 1
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
