class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        newword = ''
        for i in range(min(len1, len2)):
            newword += word1[i]
            newword += word2[i]
        
        newword += word1[len2:] if len1 > len2 else word2[len1:]
        return newword
    
solution = Solution()
word1 = 'abc'
word2 = 'pqrst'
print("merged string is:", solution.mergeAlternately(word1, word2))
