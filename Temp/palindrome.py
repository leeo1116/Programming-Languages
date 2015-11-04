def is_palindrome(s):
    char_dict = {}
    for char in s:
        if char_dict.get(char, None):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    odd_char = 0
    for value in char_dict.values():
        if not value ^ 1:
            odd_char += 1

    return odd_char < 2, char_dict


def all_palindrome(s):
    is_p, char_dict = is_palindrome(s)
    if is_p:
        even_char = ''
        odd_char = ''
        for key, value in char_dict.items():
            if value ^ 1:
                even_char += key
            else:
                odd_char += key
        return permute(even_char)
    else:
        return []


def permute(a):
    return []

