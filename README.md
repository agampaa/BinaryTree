BinaryTree
==========

Assumptions: The tree is a ordered or sorted binary tree which has the following properties:

    The left subtree of a node contains only nodes with values less than the node's value.
    The right subtree of a node contains only nodes with values greater than the node's value.
    The left and right subtree must each also be a binary search tree.


Tree.py 

Has the Class Tree and functions (Constructor, Insertion, Lookup, Least Common Ancestor)
Has the Class NonexistentError for raising custom exception when element is nonexistent

TreeTests.py

Uses the Python PyUnit module unittest.py. Pyunit is a port of Junit by Steve Purcell

Has the Class TreeTests which has the setup method that created a Tree object, inserts elements and executes unittests.
