class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        # Sorting allows us to use two pointers
        nums.sort()

        i = 0

        # Need at least 2 numbers after i
        while i < len(nums) - 2:

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])

                    # Move both pointers after finding a triplet
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # Sum too small → need a bigger number
                    left += 1

                else:
                    # Sum too large → need a smaller number
                    right -= 1

            i += 1

        return output