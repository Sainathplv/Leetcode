class Solution:
    def seqofalphainstrings(self, s: str) -> str:
        # Initialize an empty list to store alphabetic characters
        alphabets_only = []
        
        # Iterate through each character in the input string
        for char in s:
            if char.isalpha():
                # Append the alphabetic character to the list in lowercase
                alphabets_only.append(char.lower())
        
        # Sort the alphabets in alphabetical order
        sorted_alphabets = sorted(alphabets_only)
    
        # Join the sorted alphabets into a single string
        result = ''.join(sorted_alphabets)
        return result

# Example usage
s = Solution()
print("Altered alpha's:", s.seqofalphainstrings('I am learning the strings'))
