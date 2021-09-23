# array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
array = [6, 0, 4, 2, 1]

total_water = 0
for p in range(0, len(array)):
    leftP = p
    rightP = p
    maxLeft = 0
    maxRight = 0

    while leftP >= 0:
        maxLeft = max(maxLeft, array[leftP])
        leftP -= 1

    while rightP < len(array):
        maxRight = max(maxRight, array[rightP])
        rightP += 1

    currentWater = min(maxLeft, maxRight) - array[p]

    if currentWater >= 0:
        total_water += currentWater

print(total_water)
