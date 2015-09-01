__author__ = 'liangl2'
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        text = ' '.join(words)+' '
        if text == ' ':
            return [' '*maxWidth]
        justified_text = []
        while text:
            idx = text.rfind(' ', 0, maxWidth+1)
            line = text[:idx].split()
            l, n = sum(len(w) for w in line), len(line)
            if n == 1:
                justified_text.append(line[0].ljust(maxWidth))
            else:
                s, remainder = divmod(maxWidth-l, n-1)
                line[:-1] = [w+' '*s for w in line[:-1]]
                line[:remainder] = [w+' ' for w in line[:remainder]]
                justified_text.append(''.join(line))
            text = text[idx+1:]
        justified_text[-1] = ' '.join(justified_text[-1].split()).ljust(maxWidth)
        return justified_text
