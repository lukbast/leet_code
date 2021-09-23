array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

length = len(array)

total = 0
left = 0
right = length - 1
left_max = 0
right_max = 0

while left < right:
    if array[left] < array[right]:
        if array[left] < left_max:
            total += left_max - array[left]
        else:
            left_max = array[left]
        left += 1
    else:
        if array[right] < right_max:
            total += right_max - array[right]
        else:
            right_max = array[right]
        right -= 1

print(total)
