class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(arr)
        u=[]
        for x in a:
            if not u or u[-1] != x:
                u.append(x)
        for i in range(len(arr)):
            arr[i]=bisect_left(u,arr[i]) + 1
        return arr