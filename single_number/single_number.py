'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(nums):
    # Your code here

    # for loop, loop over the array
    for num in nums:

        current = 0
        match = 1

        # base case
        if len(nums) == 1:
            return nums[0]

        elif nums[current] != nums[match]:
            match += 1
        # still loops over remaining items that don't match single number, figure out how to place bounds on loop
        else:
            nums.pop(match)
            nums.pop(current)
            return single_number(nums)

    return nums[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
