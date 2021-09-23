def length_of_longest_substring(s: str):

    s_length = len(s)

    if s_length == 0:
        return 0

    letters = {}
    max_length = 0
    p1 = 0
    p2 = 0

    for p2 in range(0, s_length):
        if s[p2] not in s[p1:p2]:
            letters[s[p2]] = p2
            p2 += 1
        else:
            max_length = max(max_length, p2-p1)
            p1 = letters[s[p2]] + 1
            letters[s[p2]] = p2
            p2 += 1

    max_length = max(max_length, p2-p1)

    return max_length


print(length_of_longest_substring("a"))


