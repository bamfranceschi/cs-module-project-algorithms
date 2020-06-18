'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    # Your code here
    # need recursion

    # input into function is current cookie and desired cookie (both integers):
    # if current_cookie is greater than desired_num_cookie:
    # return 0
    # if current_cookie is less than or equal to desired_num_cookie:
    # return 1

    # create a dictionary cache
    # 1 cookie : 1
    # 2 cookies : 2
    # 3 cookies : 4
    # 4 cookies: 7

    # base case to stop recursion bc we can't have negative cookies
    if n < 0:
        return 0
    # base case
    if n == 0:
        return 1
        # if I comment out lines 32-36, tests pass also. Why is this? What's going on?
    # if n == 2:
    #     return 2

    # if n == 1:
    #     return 1

    # if cache is none
    if cache is None:
        # create the cache
        cache = {}

    # check for previously computed answer in our cache
    if n in cache:
        # return cache value of n  cache[n]
        return cache[n]

    cache[n] = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
