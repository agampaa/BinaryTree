class NonexistentError(Exception):
	"""Custom Exception thrown when least common ancestor does not exist"""
	pass

class Tree:
    def __init__(self, value=None, right=None, left=None):
    	"""
    	Tree constructor

    	@param value - current node value
    	@param right - right node of the tree
    	@param left - left node of the tree
    	"""
        self.value = value
        self.right = right
        self.left = left
 
    def __nonzero__(self):
    	"""
    	Truth value testing of a tree
    	
    	@returns False or True
    	"""
        return self.value is not None
 
    def insert(self, item):
    	"""
    	Insert new node to the tree recursively

    	@param item - new node object to insert into tree
    	"""
        if not self: # tree is empty
            self.value = item
        elif item < self.value:
            if self.left:
                return self.left.insert(item)
            else:
                self.left = Tree(value=item)
        elif item > self.value:
            if self.right:
                return self.right.insert(item)
            else:
                self.right = Tree(value=item)
        return None
    
    def lookup(self, item):
    	"""
    	Lookup node in the tree recursively

    	@param item node to look up in the tree
    	@returns True if node found in tree, if not returns False
    	"""
        if item < self.value:
            if self.left is None:
                return False
            return self.left.lookup(item)
        elif item > self.value:
            if self.right is None:
                return False
            return self.right.lookup(item)
        else:
            return True
 
    def lca(self, item1, item2):
    	"""
    	Find Least Common Common Ancestor for the given two items recursively
    	
    	@param item1 the first item of the least common ancestor to look for
    	@param item2 the second item of the least common ancestor to look for
    	"""
    	if not self.lookup(item1) or not self.lookup(item2):
    		raise NonexistentError # If item1 or item2 does not exist in the tree
        if item2 < self.value:
            return self.left.lca(item1, item2)
        elif item1 > self.value:
            return self.right.lca(item1, item2)
        else:
            return self.value
