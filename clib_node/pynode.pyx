# distutils: sources = clib_node/node.c
# distutils: include_dirs = .
from clib_node cimport cnode
from collections import deque
from random import random

cdef class Node:
    cdef cnode.Node* _c_node
    cdef Node left, right

    def __cinit__(self, int val=0, Node left=None, Node right=None):
        self._c_node = cnode.node_new(val)
        if self._c_node is NULL:
            raise MemoryError()
        if left is not None:
            self.set_left(left)
        if right is not None:
            self.set_right(right)

    def __dealloc__(self):
        if self._c_node is not NULL:
            cnode.node_free(self._c_node)

    def set_left(self, Node child):
        self.left = child
        cnode.set_left(self._c_node, child._c_node)

    def set_right(self, Node child):
        self.right = child
        cnode.set_right(self._c_node, child._c_node)

    @classmethod
    def generate_random_tree(cls, int num_nodes, double threshold=0.8):
        """Generate a random binary tree with n nodes."""
        cdef Node root = Node(0)
        cdef int cnt = 1
        queue = deque([root])
        while cnt < num_nodes and queue:
            cur = queue.popleft()
            if random() < threshold:
                left_child = Node(cnt)
                cur.set_left(left_child)
                cnt += 1
                queue.append(left_child)
            if random() < threshold:
                right_child = Node(cnt)
                cur.set_right(right_child)
                cnt += 1
                queue.append(right_child)
        return root

cdef preorder_traversal(Node root, int res[]):
    """Pre-order traversal of a tree at root node."""
    cnode.preorder_traversal(root._c_node, res, 0)

def test_preorder_traversal(num_node=20000, threshold=0.8):
    """Test preorder traversal with randomly generated tree"""
    root = Node.generate_random_tree(num_node, threshold)
    cdef int preorder[40000]
    preorder_traversal(root, preorder)