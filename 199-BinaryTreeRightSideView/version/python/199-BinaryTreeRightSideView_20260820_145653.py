# Last updated: 8/20/2026, 2:56:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        
12        queue = [root]
13        curr = 0
14        ans = []
15        
16        while curr < len(queue):
17            ans.append(queue[curr].val)
18            qSize = len(queue)
19            
20            for i in range(curr, qSize):
21                if queue[i].right:
22                    queue.append(queue[i].right)
23                if queue[i].left:
24                    queue.append(queue[i].left)
25            
26            curr = qSize
27        
28        return ans