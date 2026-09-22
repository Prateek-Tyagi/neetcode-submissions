class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for s in strs:
            encoded_string  += str(len(s)) + "#" + s
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        # need to start from the index 0
        i = 0
        while i < len(s):
            j = i
            # need to find the "#"
            while s[j] != "#":
                j += 1
            # length of string will be between i and j
            length = int(s[i:j])

            # start of the string will be just after "#"
            start = j + 1
            # end of the string will be after # + length of the string
            end = start + length

            word = s[start:end]
            decoded_strs.append(word)

            i = end
        return decoded_strs



            
        

