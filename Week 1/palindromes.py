def reverse(s):
    """ (str) -> str

    Return s reversed.

    >>> reverse('hello')
    'olleh'
    """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed
    return s_reversed


def is_palindrome_v1(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('radar')
    True
    >>> is_palindrome_v1('kayaks')
    False
    """

    s_reversed = reverse(s)
    return s == s_reversed

def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """

    # The number of chars in s.
    n = len(s)

    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n // 2] == reverse(s[n - n // 2:])


def is_palindrome_v3(s):     """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """


# s[i] and s[j] are the next pair of characters to compare.
i = 0
j = len(s) - 1

# The characters in s[:i] have been successfully compared to those in s[j:].
while i < j and s[i] == s[j]:
    i = i + 1
    j = j - 1

# If we exited because we successfully compared all pairs of characters,
# then j <= i.
return j <= i

