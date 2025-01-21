class Solution:
    def reverseVowels(self, s: str) -> str:
        # 2 pointer system
        s_list = list(s)
        print("s_list:",s_list)
        v = set('aeiouAEIOU')
        #pointers Intiallization
        left, right = 0, len(s_list) - 1

        while left< right:

            while left< right and s_list[left] not in v:
                left +=1
            while left < right and s_list[right] not in v:
                right -=1
            
            # if yes --> swap
            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1
        
        return ''.join(s_list) #list to string 

        

sol = Solution()
s = "HEiSSmart"
ans = sol.reverseVowels(s)
print(ans)