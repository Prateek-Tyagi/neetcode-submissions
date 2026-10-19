class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_frequency = {}
        for char in s1:
            target_frequency[char] = target_frequency.get(char, 0) + 1

        window_frequency = {}
        left = 0

        for right in range(len(s2)):
            
            window_frequency[s2[right]] = window_frequency.get(s2[right], 0) + 1
            window_size = right - left + 1
            if window_size > len(s1):
                window_frequency[s2[left]] -= 1
                
                if window_frequency[s2[left]] == 0:
                    del window_frequency[s2[left]]
                

                left = left + 1
                window_size = right - left + 1

            if window_size == len(s1):
                if window_frequency == target_frequency:
                    return True   
    
        return False