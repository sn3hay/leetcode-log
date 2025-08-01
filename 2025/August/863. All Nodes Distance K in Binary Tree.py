# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def createAdjList(self, node, prev, adjList):
        if prev:
            adjList[node].append(prev)
        if node.left:
            adjList[node].append(node.left)
            self.createAdjList(node.left, node, adjList)
        if node.right:
            adjList[node].append(node.right)
            self.createAdjList(node.right, node, adjList)
        return adjList
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        adjList = self.createAdjList(root, None, defaultdict(list))
        q = deque()
        q.append([target, 0])
        seen = set()
        res = []
        while q:
            node, level = q.popleft()
            seen.add(node)
            if level == k:
                res.append(node.val)
            level += 1
            for neigh in adjList[node]:
                if neigh not in seen:
                    q.append([neigh, level])
        return res




        
