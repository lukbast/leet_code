# array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
array = [6, 0, 4, 2, 1]

trapped_rainwater = 0
prev_wall = 0
i = 0
number_of_stops = 0
length = len(array)

while True:
    if i + 1 < length:
        i += 1
    else:
        if array[i] < array[prev_wall]:
            trapped_rainwater -= (array[prev_wall]-array[i]) * number_of_stops
        break

    if array[i] < array[prev_wall]:
        trapped_rainwater += array[prev_wall] - array[i]
        number_of_stops += 1
    else:
        prev_wall = i
        number_of_stops = 0

print(trapped_rainwater)
