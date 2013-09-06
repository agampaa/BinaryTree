BinaryTree
==========

Assumptions: The tree is a ordered or sorted binary tree which has the following properties:

    The left subtree of a node contains only nodes with values less than the node's value.
    The right subtree of a node contains only nodes with values greater than the node's value.
    The left and right subtree must each also be a ordered binary tree.


Tree.py
=======

    Has the Class Tree and Functions (Constructor, Insertion, Lookup, Least Common Ancestor)
    Has the Class NonexistentError for raising custom exception when element is nonexistent

TreeTests.py
============

    Uses the Python PyUnit module unittest.py. PyUnit is a port of JUnit by Steve Purcell
    
    Has the Class TreeTests which has the setup function that creates a Tree object, inserts elements and 
    executes unittests. 
    
    Testing is done for:
        Tree Creation
        Element Lookup of all the inserted elements
        Element lokkup for a non-existent element
        Test Least Common Ancestors for a tuple of nodes. In Python tuple is an immutable list or array
        Test Least Common Ancestor for a pair of items not present in the tree and verify exception is raised

How to Execute:
===============
    python TreeTests.py 
    

    
