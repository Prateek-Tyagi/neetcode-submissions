class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_frequency = {}
        for char in t:
            target_frequency[char] = target_frequency.get(char,0) + 1

        window_frequency = {}
        left = 0
        min_length = float("inf")
        min_start = 0
        required = len(target_frequency)
        formed = 0

        for right in range(len(s)):
            char = s[right]
            window_frequency[char] = window_frequency.get(char,0) + 1

            #start checking if requirement is satisfied
            if char in target_frequency:
                if window_frequency[char] == target_frequency[char]:
                    formed += 1

            # shrinking window while window is valid
            while required == formed:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    min_start = left
                
                left_char = s[left]
                window_frequency[left_char] -= 1
                if left_char in target_frequency:
                    if window_frequency[left_char] < target_frequency[left_char]:
                        formed -= 1
                left += 1
            
        if min_length == float("inf"):
                return ""
        return s[min_start: min_start + min_length]
        