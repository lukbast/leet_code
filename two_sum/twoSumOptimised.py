
def two_sum_optimised():

    arr = [1, 3, 7, 4, 8, 90, 9, 2]
    target = 1

    helper_dict = {}

    for i in range(0, len(arr)-1):
        helper_dict[target-arr[i]] = i
        if arr[i+1] in helper_dict.keys():
            return [i+1, helper_dict.get(arr[i+1])]
    return None


print(two_sum_optimised())
