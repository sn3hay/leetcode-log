import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def ssolve(root, p, q):
            if not root:
                return None
            if root ==p or root == q:
                return root
            left_subtree = ssolve(root.left, p, q)
            right_subtree = ssolve(root.right, p, q)
            
            if left_subtree and right_subtree:
                return root
            if left_subtree:
                return left_subtree
            return right_subtree
        return ssolve(root, p, q)

        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.root = TreeNode(3)
        self.node5 = TreeNode(5)
        self.node1 = TreeNode(1)
        self.node6 = TreeNode(6)
        self.node2 = TreeNode(2)
        self.node0 = TreeNode(0)
        self.node8 = TreeNode(8)
        self.node7 = TreeNode(7)
        self.node4 = TreeNode(4)

        self.root.left = self.node5
        self.root.right = self.node1
        self.node5.left = self.node6
        self.node5.right = self.node2
        self.node1.left = self.node0
        self.node1.right = self.node8
        self.node2.left = self.node7
        self.node2.right = self.node4
        
    def test_LCA_common_case(self):
        lca = self.solution.lowestCommonAncestor(self.root, self.node5, self.node1)
        self.assertEqual(lca, self.root)
        
    def test_LCA_descendant_case(self):
        lca = self.solution.lowestCommonAncestor(self.root, self.node5, self.node4)
        self.assertEqual(lca, self.node5)
        
    def test_LCA_same_node(self):
        lca = self.solution.lowestCommonAncestor(self.root, self.node4, self.node4)
        self.assertEqual(lca, self.node4)
        
    
if __name__ == '__main__':
    unittest.main()
        
        
    
        


            
        
        
        
        
