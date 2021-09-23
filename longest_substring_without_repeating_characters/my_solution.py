test_string = "bpfbhmipx"

prev_substring = ""
present_length = 0
max_length = 0

for i, letter in enumerate(test_string):
    if letter not in prev_substring:
        present_length += 1
        prev_substring += letter
    else:
        pointer = len(prev_substring) - 1
        next_substring = ""
        next_length = 0
        while pointer >= 0:
            if prev_substring[pointer] == letter:
                break
            next_substring += prev_substring[pointer]
            next_length += 1
            pointer -= 1

        if present_length > max_length:
            max_length = present_length
        present_length = next_length + 1
        prev_substring = next_substring[::-1] + letter
else:
    if present_length > max_length:
        max_length = present_length

print(max_length)
