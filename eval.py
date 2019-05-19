import time
from random import seed

from pysrc.node import test_preorder_traversal
from pysrc_as_pyx.cnode import test_preorder_traversal as test_preorder_traversal_v2
from pysrc_static_typing.cnode import test_preorder_traversal as test_preorder_traversal_v3
from clib_node.pynode import test_preorder_traversal as test_preorder_traversal_v4

if __name__ == '__main__':
    NUM_TRAILS = 100
    BEGIN = time.time()
    for i in range(NUM_TRAILS):
        seed(i)
        test_preorder_traversal()
    END = time.time()
    DURATION = END - BEGIN
    print "Python finishes in {} seconds - {} s/run".format(DURATION, DURATION / NUM_TRAILS)

    BEGIN = time.time()
    for i in range(NUM_TRAILS):
        seed(i)
        test_preorder_traversal_v2()
    END = time.time()
    DURATION = END - BEGIN
    print "Cython pysrc as pyx finishes in {} seconds - {} s/run".format(DURATION, DURATION / NUM_TRAILS)

    BEGIN = time.time()
    for i in range(NUM_TRAILS):
        seed(i)
        test_preorder_traversal_v3()
    END = time.time()
    DURATION = END - BEGIN
    print "Cython static typing finishes in {} seconds - {} s/run".format(DURATION, DURATION / NUM_TRAILS)

    BEGIN = time.time()
    for i in range(NUM_TRAILS):
        seed(i)
        test_preorder_traversal_v4()
    END = time.time()
    DURATION = END - BEGIN
    print "Cython C-lib finishes in {} seconds - {} s/run".format(DURATION, DURATION / NUM_TRAILS)
