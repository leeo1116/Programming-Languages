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
        permutation = permute(even_char)
        all_p = []
        for p in permutation:
            all_p.append(p+odd_char+p[::-1])
        return all_p
    else:
        return []


def permute(s):
    if len(s) <= 1:
        return [s]
    else:
        permutation = []
        for i in range(len(s)):
            for p in permute(s[:i]+s[i+1:]):
                permutation.append(s[i]+p)
        return permutation

print(all_palindrome("abcbc"))