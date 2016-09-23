class Solution(object):
    def product_exclude_itself(self, A):
        left_tmp, right_tmp, left_product, product = 1, 1, [1]*len(A), [1]*len(A)
        for i in range(len(A)):
            left_product[i] = left_tmp
            left_tmp *= A[i]
        for j in range(len(A))[::-1]:
            product[j] = left_product[j]*right_tmp
            right_tmp *= A[j]
        return product

s = Solution()
print(s.product_exclude_itself([]))

