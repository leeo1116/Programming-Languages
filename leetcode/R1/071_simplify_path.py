__author__ = 'liangl2'
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        result = []
        path_list = path.split('/')
        for content in path_list:
            if content:
                if content == "..":
                    try:
                        result.pop()
                    except:
                        result = []
                elif content != '.':
                    result.append(content)
        return '/'+'/'.join(result)

s = Solution()
print(s.simplifyPath("/a/./c/"))