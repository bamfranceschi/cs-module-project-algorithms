'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    for el in arr:  # O(n)
        if el == 0:
            arr.remove(el)
            arr.append(el)

    return arr


# two pointers?
'''
    what if we had a pointer that started at the beginning and a pointer that started at the end and they moved towards each other in the middle?

    if the left pointer "sees" a zero and the right pointer "sees" a non-zero, swap

    if the left sees a non-zero increment
    if the right sees a zero increment
'''

# left pointer at the beginning
# right pointer at end

# loop until left and right pointers meet or right pointer passes left pointer O(n)
# right pointer is < left pointer
# swap situation:
# left sees zero and right sees non-zero
# swap the items
# increment left
# decrement right
# non-swap situation
# if left sees non-zero
# increment left
# if right sees zero
# decrement
# return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
