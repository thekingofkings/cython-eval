import time
from random import seed

from clib_node.pynode import test_preorder_traversal as test_preorder_traversal_v4

if __name__ == '__main__':
    NUM_TRAILS = 1
    BEGIN = time.time()
    for i in range(NUM_TRAILS):
        seed(i)
        test_preorder_traversal_v4(num_node=5)
    END = time.time()
    DURATION = END - BEGIN
    print "Cython C-lib finishes in {} seconds - {} s/run".format(DURATION, DURATION / NUM_TRAILS)