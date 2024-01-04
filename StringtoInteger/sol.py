class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Initialize variables
        i, n, sign, result = 0, len(s), 1, 0

        # 1. Read in and ignore any leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check the next character for '+' or '-'
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Read in the next characters until the next non-digit character
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Apply the final logic to clamp the value within the 32-bit range
        result = sign * result
        result = min(result, INT_MAX)
        result = max(result, INT_MIN)

        return result

solution = Solution()

# Define test cases
test_cases = ["4193 with words", "   -42", "1234", "words and 987", "+100", "2147483648"]

# Test each case
for test in test_cases:
    result = solution.myAtoi(test)
    print(f"Input: '{test}' -> Output: {result}")