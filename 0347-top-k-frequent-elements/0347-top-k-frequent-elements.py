class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        mf = {}
        for i in range(len(nums)):
            if nums[i] not in mf:
                mf[nums[i]] = mf.get(nums[i],0)+1
            else:
                mf[nums[i]]+=1
        mff = dict(sorted(mf.items(), key=lambda item:item[1] , reverse = True))
        r = []
        c=0
        while c<k:
            r.append(list(mff.keys())[c])
            c+=1
        r.sort()
        return r    