class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s_len = len(secret)
        bulls_count, cows_count = 0, 0
        schar_freq_dict = {}
        gchar_freq_dict = {}
        for i in range(s_len):
            if secret[i] == guess[i]:
                bulls_count += 1
            else:
                if schar_freq_dict.get(guess[i], None):
                    cows_count += 1
                    schar_freq_dict[guess[i]] -= 1
                else:
                    gchar_freq_dict[guess[i]] = gchar_freq_dict.get(guess[i], 0) + 1
                if gchar_freq_dict.get(secret[i], None):
                    cows_count += 1
                    gchar_freq_dict[secret[i]] -= 1
                else:
                    schar_freq_dict[secret[i]] = schar_freq_dict.get(secret[i], 0) + 1

        return str(bulls_count)+'A'+str(cows_count)+'B'


s = Solution()
print(s.getHint("2962", "7236"))