import re


def remove_junk(s:str) -> str:

    pattern = re.compile('[\W_]+')
    s = re.sub(pattern, "", s).lower()
    return s


def palindrome(s: str) -> bool:

    if s == "":
        return True
    if len(s) == 1:
        return True

    p1 = 0
    p2 = len(s)-1

    while p1 <= p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True
