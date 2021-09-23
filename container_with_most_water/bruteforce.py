array = [7, 1, 2, 3, 9]


def get_max_water_container(arr):

    max_area = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                processed_area = arr[i]*(j-i)
            else:
                processed_area = arr[j]*(i-j)

            if processed_area > max_area:
                max_area = processed_area
    return max_area


print(get_max_water_container(array))
