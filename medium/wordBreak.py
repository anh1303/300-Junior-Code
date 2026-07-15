class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0]= True
        wordSet = set(wordDict)
        
        # for i in range(1, len(s) + 1):
        #     for word in wordSet:
        #         w_len = len(word)
        #         if i >= w_len and dp[i - w_len]:
        #             if s[i- w_len : i] == word:
        #                 dp[i] = True
        #                 break
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
                
        return dp[len(s)]