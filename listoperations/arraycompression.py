class Solution:
    def compress(self, chars):
        # Pointers for writing and reading
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]  # Current character
            count = 0
            
            # Count consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the array
            chars[write] = char
            write += 1
            
            # If count > 1, write the digits of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write


# Main function to get user input
def main():
    # Ask the user for the input
    user_input = input("Enter the characters of the array separated by spaces (e.g., 'a a b b c c c'): ")
    
    # Convert input into a list of characters
    chars = user_input.split()
    
    # Ensure the input is not empty
    if not chars:
        print("Error: Input array cannot be empty.")
        return
    
    # Create an instance of the solution and compress the array
    solution = Solution()
    new_length = solution.compress(chars)
    
    # Print the results
    print(f"Compressed Length: {new_length}")
    print(f"Compressed Array: {chars[:new_length]}")

# Run the main function
if __name__ == "__main__":
    main()