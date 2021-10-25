class Solution:
    def findMedianSortedArrays(self, nums: List[int], mums: List[int]) -> float:
        if len(mums) < len(nums):
            mums, nums = nums, mums

        if len(mums) == 0:
            return 0

        if len(nums) == 0:
            if len(mums) % 2:
                return mums[len(mums) // 2]
            else:
                return (mums[len(mums) // 2 - 1] + mums[len(mums) // 2]) / 2

        ml, nl = len(mums), len(nums)
        Mid, i, j = (ml + nl) // 2, 0, nl-1

        while True:
            n = (i + j) // 2
            m = Mid - n - 2

            mleft = mums[m] if m > -1 else -9999999
            nleft = nums[n]  if n > -1 else -9999999
            mright = mums[m+1] if m+1 < ml else 9999999
            nright = nums[n+1] if n+1 < nl else 9999999
 
            if mleft <= nright  and nleft <= mright:
                if (ml + nl) % 2:
                    return min(mright, nright) 
                else:
                    return (max(mleft, nleft) + min(mright, nright)) / 2
            elif mleft > nright :
                i = n+1
            else:
                j = n-1


        # Naive (Other than this you can merge the two array in O(n + m)
        nList = sorted(nums + mums)
        if len(nList) % 2:
            return nList[len(nList) // 2]
        else:
            return (nList[len(nList) // 2 - 1] + nList[len(nList) // 2]) / 2
 
