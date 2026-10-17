class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 
        B = nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        # we binary search smaller array
        left = 0
        right = len(A)

        while left <= right:
            # cut the Smaller array
            cutA = (left + right) // 2
            # cut the bigger Arry
            cutB = half - cutA 

            # get the values around these cuts

            Aleft = A[cutA - 1] if cutA > 0 else float("-inf")
            Aright = A[cutA] if cutA < len(A) else float("inf")

            Bleft = B[cutB -1 ] if cutB > 0 else float("-inf")
            Bright = B[cutB] if cutB < len(B) else float("inf")

            # find if its a good cut - 

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = cutA - 1
            else:
                left = cutA + 1