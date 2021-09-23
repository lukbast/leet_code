first = "a###b"
second = "b"


def typed_out_strings(s, t):

    p = len(s) - 1
    s_result = []
    t_result = []
    backslashes = 0

    while p > -1:
        if s[p] == "#":
            backslashes += 1
        elif backslashes > 0:
            backslashes -= 1
        else:
            s_result.append(s[p])

        p -= 1

    backslashes = 0
    p = len(t) - 1

    while p > -1:
        if t[p] == "#":
            backslashes += 1
        elif backslashes > 0:
            backslashes -= 1
        else:
            t_result.append(t[p])

        p -= 1

    result = s_result == t_result
    return result


print(typed_out_strings(first, second))
