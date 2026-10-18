class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        longest = 0
        left = 0

        for right in range(len(s)):

            frequency[s[right]] = frequency.get(s[right],0) + 1
            maxFrequency = max(frequency.values())
            window_size = right - left + 1

            while window_size - maxFrequency > k:
                frequency[s[left]] -= 1
                left +=1

                maxFrequency = max(frequency.values())
                window_size = right - left + 1
            
            longest = max(longest, window_size)

        return longest
        