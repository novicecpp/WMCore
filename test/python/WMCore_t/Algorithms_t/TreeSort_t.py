#!/usr/bin/env python2.4
"""

"""

__revision__ = "$Id: TreeSort_t.py,v 1.1 2009/04/24 21:36:01 swakef Exp $"
__version__ = "$Revision: 1.1 $"

import unittest
from WMCore.Algorithms.TreeSort import TreeSort

_name = lambda x: x['name']
_parents = lambda x: x['parents']

class TreeSortTest(unittest.TestCase):
    """
    _TreeSortTest_
    
    """

    def testNullOp(self):
        """
        Test case where input already sorted
        """
        items = [ {'name' : 'Node1', 'parents' : []},
                   {'name' : 'Node2', 'parents' : ['Node1']},
                   {'name' : 'Node3', 'parents' : ['Node2']} ] 
        results = TreeSort(_name, _parents, items[:]).sort()
        self.assertEqual(results, items)


    def testSimpleCase(self):
        """
        Simple case with input items that can be sorted
        """
        items = [ 
                 {'name' : 'Node4', 'parents' : ['Node1']},
                 {'name' : 'Node1', 'parents' : []},
                 {'name' : 'Node3', 'parents' : ['Node2']},
                 {'name' : 'Node2', 'parents' : ['Node1']}] 
        answer = [{'parents': [], 'name': 'Node1'},
                  {'parents': ['Node1'], 'name': 'Node2'},
                  {'parents': ['Node2'], 'name': 'Node3'},
                  {'parents': ['Node1'], 'name': 'Node4'}]
        results = TreeSort(_name, _parents, items).sort()
        self.assertEqual(results, answer)
        
        
    def testMultipleParents(self):
        """
        Input item has multiple parents - not supported
        
        """
        items = [ 
                 {'name' : 'Node1', 'parents' : []},
                 {'name' : 'Node2', 'parents' : ['Node1']},
                 {'name' : 'Node3', 'parents' : ['Node1', 'Node2']}] 
        self.assertRaises(RuntimeError, TreeSort, _name, _parents, items)
        
        
    def testExternalParent(self):
        """
        parents that arent in the input are ignored by the sort algorithm
        Assumption is that the external dependency has already been dealt 
        with by client
        """
        items = [ 
                 {'name' : 'Node2', 'parents' : ['Node1']},
                 {'name' : 'Node1', 'parents' : ['Node0']},
                 {'name' : 'Node3', 'parents' : ['Node2']}] 
        answer = [{'parents': ['Node0'], 'name': 'Node1'},
                  {'parents': ['Node1'], 'name': 'Node2'},
                  {'parents': ['Node2'], 'name': 'Node3'}]
        result = TreeSort(_name, _parents, items).sort()
        self.assertEqual(result, answer)
        

    def testUnsorteable(self):
        """
        Input cannot be sorted with this algorithm
        """
        items = [ 
                 {'name' : 'Node1', 'parents' : ['Node2']},
                 {'name' : 'Node2', 'parents' : ['Node1']}] 
        self.assertRaises(RuntimeError, TreeSort, _name, _parents, items)
        

    def runTest(self):
        self.testNullOp() 
        self.testSimpleCase()
        self.testMultipleParents()
        self.testExternalParent()
        self.testUnsorteable()

if __name__ == "__main__":
    unittest.main()