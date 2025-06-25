# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append((root,None))
        while q:
            n = len(q)
            lsum = 0
            for node in q:
                lsum += node[0].val
            spar = q[0][1]
            #print("par",spar)
            csum = lsum
            print("lsum ",lsum)
            #print(csum)
            q1 =deque()
            while n > 0 :
                tup = q.popleft()
                node = tup[0]
                par = tup[1]
                #print("par",par)
                if node.left:
                    q.append((node.left,node))
                if node.right:
                    q.append((node.right,node))
                if par == spar:
                    csum -= node.val
                    q1.append(node)
                else:
                    while q1:
                        ch = q1.popleft()
                        ch.val = csum
                    csum = lsum - node.val
                    spar = par
                    print(node.val, csum)
                    q1.append(node)
                n-=1
            if q1:
                while q1:
                    ch = q1.popleft()
                    ch.val = csum
                
        return root
        
            
                
                
            
            
            
        
        
