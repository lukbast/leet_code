arr = [1, 3, 7, 9, 2]
target = 11


def sum_two_brute_force():
    if len(arr) >= 2:
        for i in range(0, len(arr)-1):
            search_value = target - arr[i]
            for j in range(i+1, len(arr)):
                if arr[j] == search_value:
                    return [i, j]
    else:
        return None


print(sum_two_brute_force())
