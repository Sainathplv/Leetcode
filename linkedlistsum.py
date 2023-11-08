# first i wanna create a linked list 

# function for linked list initalliation as let me create a object 
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def addition(l1,l2):
        #(l1:[ListNode],l2:[ListNode])-> [ListNode]
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            value1 = l1.value if l1 else 0
            value2 = l2.value if l2 else 0
            # adding and storing a value in a dummy node

            value = value1+value2+carry
            carry = value//10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
def create_list(elements):
        dummy = ListNode(0)
        current = dummy
        for element in elements:
            current.next = ListNode(element)
            current = current.next
        return dummy.next
def get_list_input():
        input_values = input("Enter the elements of the list separated by space: ")
        elements = list(map(int, input_values.strip().split()))
        return create_list(elements)
def print_list(node):
        while node:
            print(node.value, end=' ')
            node = node.next
        print()
# Get user input to create the list
print("Please provide the first list:")
l1 = get_list_input()
print("Please provide the second list:")
l2 = get_list_input()
    # Add the lists
result = addition(l1, l2)
    # Print the result
print("The resulting list after adding elements by index is:")
print_list(result)            
