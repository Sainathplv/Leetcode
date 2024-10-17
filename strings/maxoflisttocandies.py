class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bol= []
        maximum = max(candies)
        for i in candies:
            bol.append(i+extraCandies >= maximum)
        return bol

solution = Solution()
b = [1,5,6,7,8]
ex = 10
a = solution.kidsWithCandies(b,ex)
print(a)            
        
        