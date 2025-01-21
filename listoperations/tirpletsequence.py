class Solution:
    def increasingTriplet(self, nums):
        # Initialize variables to track the smallest and second smallest elements
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                # Update the smallest element
                first = num
            elif num <= second:
                # Update the second smallest element
                second = num
            else:
                # If a number is greater than second, a triplet exists
                return True
        
        # If no such triplet is found
        return False


# Main function to get user input
def main():
    # Ask user for the length of the array
    n = int(input("Enter the length of the array: "))
    
    # Ensure the length is at least 3
    if n < 3:
        print("Array must have at least 3 elements to check for a triplet.")
        return
    
    # Input the array elements
    print(f"Enter {n} integers separated by space:")
    nums = list(map(int, input().split()))
    
    # Validate the input length
    if len(nums) != n:
        print(f"Error: You must enter exactly {n} integers.")
        return
    
    # Create an instance of Solution and check for the triplet
    solution = Solution()
    result = solution.increasingTriplet(nums)
    
    # Output the result
    if result:
        print("True: There exists a triplet (i, j, k) such that nums[i] < nums[j] < nums[k].")
    else:
        print("False: No such triplet exists.")

# Run the main function
if __name__ == "__main__":
    main()