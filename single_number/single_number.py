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

# Matt's solution:
    # no_dups = [] O(n)

    # for num in nums: O(n)
    #     if num not in no_dups: O(n)
    #         no_dups.append(num)
    #     else:
    #         no_dups.remove(num) O(n)

    # return no_dups[0]

# mathias skreden's solution:
# def single_number(arr):
#     for elem in arr:
#         if arr.count(elem) == 1:
#             return elem

# Matt's second solution:
# keep track of numer of times an item occurs in input
    #counts = {}

    # loop through input list O(n)
    # for num in nums:
    # check if item is in counts O(1)
    # if num in counts:
    # if it is, increment the count
    #num += 1
    # if item is not in counts
    # else:
    # set item count to 1
    #num = 1

    # loop through dictionary and find the key/value where value is 1
    # for k, v in counts.items(): O(n)
    # if v == 1:
    # return k


# Jud's solution
    #for num in nums: O(n)
    # if num in counts:
    #del counts[num]
    # else:
    #counts[num] = 1
    # return counts[counts.keys()[0]]
# optional:
    # for k, v in counts.items(): O(n)
    # if v == 1:
    # return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
