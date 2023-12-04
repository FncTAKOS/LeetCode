class Solution(object):
    def largestGoodInteger(self, num):
        res=0
        for i in range(len(num)-2):
            if(num[i]==num[i+1]==num[i+2]):
                res=max(res,num[i])
        return "" if res==0 else str(res)*3