class Solution:
    def longestPalindrome(self, s: str) -> str:
        #check the size and length of a string
        if(len(s)<=1):
            return s
        # intialize the ma strand length to1 and first element
        Max_str = s[0]
        Max_len = 1
        for i in range(len(s)-1):
             #if i=0 and j=1 at len of string is 2
             for j in range(i+1,len(s)):#check all the values of a string one by one by augmenting
                 if j - i + 1 > Max_len  and  s[i:j + 1] == s[i:j + 1][::-1]:
                     Max_len = j-i+1
                     Max_str = s[i:j+1]
        return Max_str

