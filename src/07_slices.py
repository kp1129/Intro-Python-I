"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
def middle_elements(lst):
    if len(lst) % 2 == 1:
        # if the list has an odd number of elements
        # grab the middle element
        return lst[int(len(lst) / 2)]
    else:
        # if the list has an even number of elements
        # find the middle and grab
        # the element to the right and the element to the left
        return lst[int(len(lst) / 2) -1 : int(len(lst) / 2) +1]    

print(middle_elements(a))

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])