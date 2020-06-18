'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # pointers we need
    all_maxes = []
    start_k = 0
    end_k = k - 1
    max_value_in_k = nums[start_k]

    # need nested for loops - one to traverse the main array

    for num in nums:

        pointer = start_k + 1

        # and one to traverse k

        for val in nums[start_k:end_k]:

            if max_value_in_k < nums[pointer]:
                max_value_in_k = nums[pointer]
                pointer += 1

            elif max_value_in_k >= nums[pointer]:
                pointer += 1
        # once max value is found, append to empy array
        all_maxes.append(max_value_in_k)

        start_k += 1
        max_value_in_k = nums[start_k]

        if end_k != (len(nums) - 1):
            end_k += 1
        else:
            return all_maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
