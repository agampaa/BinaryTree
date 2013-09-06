import Tree
import unittest

elements = (7, 2, 9, 0, 5, 13, 3, 6) # Elements used in creating a binary search tree
lca_pairs = ((3, 6), (3, 9), (0, 3), (0, 2), (3, 3)) # Least common ancestor pairs to search
lca_expect = (5, 7, 2, 2, 3) # Least common ancestor expected for the above tuple

class TreeTests(unittest.TestCase):
	def setUp(self):
		"""
		Create a tree and insert elements into the tree
		"""
		self.t = Tree.Tree()
		for elem in elements:
			self.t.insert(elem)
		
	def testTreeCreated(self):
		"""
		Test that tree is created
		"""
		self.assertNotEqual(None, self.t)
	
	def testLookupElements(self):
		"""
		Test all the inserted elements are present by looking up
		"""
		for elem in elements:
			self.assertEqual(True,self.t.lookup(elem))
			
	def testElementNotPresent(self):
		"""
		Test for element not present in the tree
		"""	
		self.assertEqual(False, self.t.lookup('s'))
	
	def testLeastCommonAncestor(self):
		"""
		Test Least Common Ancestors for all the pairs return expected values
		"""
		for expect,pair in zip(lca_expect, lca_pairs): # Iterate over multiple tuples at the same time using zip
			self.assertEqual(expect, self.t.lca(*pair))
	
	def testLeastCommonAncestorNotPresent(self):
		"""
		Test NonexistentError Exception is raised when looking for Least Common Ancestor of non-existent elements
		"""
		self.assertRaises(Tree.NonexistentError, self.t.lca, *(1,4))

if __name__ == "__main__":
	unittest.main()
