def count_characters(s: str):
    # Dictionary to store the count of each character
    char_count = {}

    # Loop through each character in the string
    for char in s:
        # Increment the count if the character is already in the dictionary
        if char in char_count:
            char_count[char] += 1
        else:
            # Otherwise, initialize the count for this character
            char_count[char] = 1

    # Create the result in the format [a:count,b:count,...]
    # result = [f"{char}:{count}" for char, count in char_count.items()]
    
    # Print the result as a list
    print(char_count)

# Example usage:
s = "abracadabra"
count_characters(s)
