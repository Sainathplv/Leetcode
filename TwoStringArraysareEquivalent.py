class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concatstr1= ''.join(word1)
        concatstr2=''.join(word2)
        return concatstr1 == concatstr2
        
