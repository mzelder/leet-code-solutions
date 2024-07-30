# My solution
   class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 
        }
        n = len(s)
        result = 0
        i = 0
    
        if n <= 1:
            return roman[s[0]]
        while i < n - 1:
            current_char = s[i]
            next_char = s[i+1]
            if current_char == "I" and next_char in ("V", "X"):
                result += roman[next_char] - roman[current_char]
                i += 1
            elif current_char == "X" and next_char in ("L", "C"):
                result += roman[next_char] - roman[current_char]
                i += 1
            elif current_char == "C" and next_char in ("D", "M"):
                result += roman[next_char] - roman[current_char]
                i += 1
            else:
                if i == n - 2: 
                    result += roman[next_char]
                result += roman[current_char]
                
            i += 1
        
        return result

# GPT solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            # If we're at the last character or the current character is not less than the next one
            if i == n - 1 or roman[s[i]] >= roman[s[i + 1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]]
        
        return result
