class Solution(object):
    def delete_digits(self, A, k):
        if len(A) == 0 or len(A) == 1 and k >= 1:
            return 0
        elif len(A) == 1 and k < 1:
            return int(A)

        A, i = list(A), 1
        while i < len(A) and len(A) > 1:
            if int(A[i]) < int(A[i-1]) and k > 0 or A[i-1] == '0':
                if A[i-1] != '0':
                    k -= 1
                A.pop(i-1)
                if i > 1:
                    i -= 1
                else:
                    i = 1
                continue
            elif k == 0:
                return ''.join(A).lstrip('0')
            i += 1
        return ''.join(A[:-k])

    def delete_digits_stack(self, A, k):
        if k < 1:
            return int(A)
        if len(A) <= k:
            return 0

        digits_stack = []
        for i in range(len(A)):
            digit = int(A[i])
            while digits_stack and digit < digits_stack[-1] and len(digits_stack)+len(A)-i-1 > len(A)-k:
                digits_stack.pop()
            if len(digits_stack) < len(A)-k:
                digits_stack.append(digit)

        min_digits = []
        while digits_stack:
            min_digits.insert(0, digits_stack.pop())

        while min_digits and min_digits[0] == 0:
            min_digits.pop(0)

        return ''.join(map(str, min_digits))


s = Solution()
print(s.delete_digits_stack("10009876091", 4))

