def length_of_longest_substring(s: str):
    s_length = len(s) - 1
    if len(s) <=1:
        return len(s)

    longest = 0
    for left in range(0, s_length):
        seen_chars = {}
        curr_length = 0
        for right in range(left, s_length):
            curr_char = s[right]
            if curr_char not in seen_chars:
                curr_length += 1
                seen_chars[curr_char] = True
                longest = max(longest, curr_length)
            else:
                break
    return longest


print(length_of_longest_substring("abcabcbb"))