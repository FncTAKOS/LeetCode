class Solution(object):
    def inorderTraversal(self, root):
        
        def findroot(root,res):
            if(root!=None):
                findroot(root.left,res)
                res.append(root.val)
                findroot(root.right,res)

        res=[]
        findroot(root,res)
        return res