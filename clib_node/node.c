#include<stdlib.h>
#include<stdio.h>
#include"node.h"

typedef struct _Node {
    int val;
    struct _Node *left;
    struct _Node *right;
} Node;

Node *node_new(int val) {
    Node *p = (Node *) malloc(sizeof(Node));
    p->val = val;
    p->left = NULL;
    p->right = NULL;
    printf("cNode %d\n", val);
    return p;
}

void node_free(Node *node) {
    if (node != NULL) {
        printf("Free node %d\n", node->val);
        free(node);
        node = NULL;
    }
}

void set_left(Node *node, Node *left) {
    printf("set left: %d -> %d\n", node->val, left->val);
    node->left = left;
}

void set_right(Node *node, Node *right) {
    printf("set right: %d -> %d\n", node->val, right->val);
    node->right = right;
}

int preorder_traversal(Node *node, int result[], int i) {
    printf("Fill result array position %d ", i);
    if (node == NULL) {
        printf(" empty node. abort with next index %d\n", i);
        return i;
    }
    printf("with value %d\n", node->val);
    result[i] = node->val;
    i += 1;
    int j = preorder_traversal(node->left, result, i);
    int k = preorder_traversal(node->right, result, j);
    return k;
}

// test correctness of node.c
int main(int argc, char *argv[]) {
    Node *root = node_new(1);
    Node *l1 = node_new(-10);
    Node *r1 = node_new(200);
    set_left(root, l1);
    set_right(root, r1);
    Node *l2 = node_new(-123);
    set_left(l1, l2);
    Node *r2 = node_new(0);
    set_right(l1, r2);

    int results[5];
    int last_index = preorder_traversal(root, results, 0);

    for (int i = 0; i < 5; i++) {
        printf("%d\n", results[i]);
    }
    printf("Returned last index is %d\n", last_index);
    node_free(root);
}