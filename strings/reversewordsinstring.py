class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words and remove any extra spaces
        x = s.split()  # This splits by spaces and removes extra spaces
        # Reverse the list of words
        x.reverse()
        # Join the words with a single space between them
        new_string = ' '.join(x)
        
        return new_string

sol  = Solution()
s = 'I am leraning strings'
ans = sol.reverseWords(s)
print(ans)