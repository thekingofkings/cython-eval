cdef extern from "node.h":
    ctypedef struct Node:
        pass

    Node *node_new(int val)
    void node_free(Node *node)
    void set_left(Node *node, Node *left)
    void set_right(Node *node, Node *right)
    int preorder_traversal(Node *node, int result[], int i)
