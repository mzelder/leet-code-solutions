class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n_arr = len(strs)
        n_first = len(strs[0])
        prefix = ""

        # We always trying compare other words to first one   
        try:    
            i = 0
            while i < n_first: 
                letter = strs[0][i]
            
                # Going through each word
                j = 1
                while j < n_arr:
                    current_letter = strs[j][i]
                    if letter != current_letter:
                        return prefix
                    j += 1
                i += 1
        
                # Add letter to prefix
                prefix += letter   
        
        # if the first word will be longer from any other word in array
        # then the indexError occur, so this is the end of our prefix
        except IndexError:
            return prefix
            
        else:
            return prefix
