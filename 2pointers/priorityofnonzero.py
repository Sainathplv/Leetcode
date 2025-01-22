class Solution:
    def moveZeroes(self, nums):
        # Pointer for the position of the next non-zero element
        non_zero_index = 0

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the element at non_zero_index
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1


# Main function to get user input
def main():
    # Ask user for the input
    user_input = input("Enter the integers in the array separated by spaces: ")
    
    # Convert the input string into a list of integers
    nums = list(map(int, user_input.split()))
    
    # Create an instance of the solution and move zeroes
    solution = Solution()
    solution.moveZeroes(nums)
    
    # Print the updated array
    print("Updated Array:", nums)

# Run the main function
if __name__ == "__main__":
    main()