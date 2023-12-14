class Solution:
    def reverse(self,x: int) -> int:
        # Define the 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle the sign and reverse the digits
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1])

        # Check for overflow
        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0

        # Return the reversed number with the original sign
        return sign * reversed_num

