Evaluate the performance of Cython
==================================


Task
----
The evaluation task is binary tree preorder traversal. We first randomly generate a binary tree with up to `num_node` nodes, where each node contain an integer value and references to left and right children. The children are generated with a probability `threshold`, and could be missing. Then we preorder traverse the whole tree.

The above process is repeated for `NUM_TRAILS` times to get average running time. The `eval.py` is used for running time evaluation.


Implementations
---------------

We compare the following four implementations.


### Pure Python Source
This is the baseline method without using Cython. It is implemented inside `pysrc` folder.


### Pure Python Source Compiled with Cython
Directly change the python source above into `pyx` file, and use Cython to compile into binary executable. It is implemented in the `pysrc_as_pyx` folder.


### Cython with Static Typing
Use static typing in the Cython `Node` class. The `cdef class Node` will be automatically compiled as a C `struct`. Implemented in `pysrc_static_typing`.



### External C library

Implement `struct Node` in a C file. Use Cython to create a pynode wrapper, so that we can use this C struct inside python code. Implemented in `clib_node`.


Results
-------
Generate tree with 20,000 nodes. The probability to attach a child node is 0.8. Run the generation/traversal 100 times to report averge running time.
```
$ python eval.py
Python finishes in 2.04210996628 seconds - 0.0204210996628 s/run
Cython pysrc as pyx finishes in 1.47619199753 seconds - 0.0147619199753 s/run
Cython static typing finishes in 0.489957094193 seconds - 0.00489957094193 s/run
Cython C-lib finishes in 0.45839381218 seconds - 0.0045839381218 s/run
```
