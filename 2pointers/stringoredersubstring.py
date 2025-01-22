class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for the string `s`
        print(f"Checking if '{s}' is a subsequence of '{t}':")
        for char in t:
            # Display comparison at each step
            if i < len(s):
                print(f"Comparing s[{i}]='{s[i]}' with t_char='{char}'")
                if s[i] == char:
                    print(f"Match found for s[{i}]='{s[i]}'")
                    i += 1  # Move to the next character in `s`

        # Final decision
        is_subsequence = i == len(s)
        print(f"\nResult: {'True' if is_subsequence else 'False'}")
        return is_subsequence


# Main function to get user input and show the output
def main():
    # Input strings from the user
    s = input("Enter the first string (s): ")
    t = input("Enter the second string (t): ")
    
    # Create an instance of the solution
    solution = Solution()
    result = solution.isSubsequence(s, t)
    
    # Print the final result
    if result:
        print(f"\n'{s}' is a subsequence of '{t}'.")
    else:
        print(f"\n'{s}' is NOT a subsequence of '{t}'.")

# Run the main function
if __name__ == "__main__":
    main()