def fn(arr):
    def check(x):
        return BOOLEAN


    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER

    while left <= right:
        mid = (left+right)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1

    return left
