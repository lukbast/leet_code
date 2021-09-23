import re


def almost_palindrome(s: str) -> bool:

    reversed_s = s[::-1]

    if s == reversed_s:
        return True

    for i in range(len(s)):
        if s[i] != reversed_s[i]:
            pointer1 = len(s) - 1 - i
            pointer2 = i
            s1 = s[:pointer1] + s[pointer1+1:]
            s2 = s[:pointer2] + s[pointer2+1:]
            return s1 == s1[::-1] or s2 == s2[::-1]


print(almost_palindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
