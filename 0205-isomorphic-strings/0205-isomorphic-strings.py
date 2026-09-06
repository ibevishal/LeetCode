class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                dic[s[i]] = t[i]

        return len(set(dic.values())) == len(dic)  # doubt helped by else