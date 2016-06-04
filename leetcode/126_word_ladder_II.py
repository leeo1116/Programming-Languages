class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        distance_word_dict = {}
        ladder_list = []
        for w in wordlist:
            distance = self.word_distance(beginWord, w)
            if distance == 0:
                return ladder_list.append([w])
            if distance_word_dict.get(distance, None):
                distance_word_dict[distance].append(w)
            else:
                distance_word_dict[distance] = [w]

        while distance_word_dict[1]:



        for i, w1 in enumerate(ladder_list[1]:
            ladder_list += [w1]
        for key, value in distance_word_dict.items():



    def word_distance(self, word1, word2):
        word_len = len(word1)
        distance = 0
        for i in range(word_len):
            if word1[i] != word2:
                distance += 1
        return distance