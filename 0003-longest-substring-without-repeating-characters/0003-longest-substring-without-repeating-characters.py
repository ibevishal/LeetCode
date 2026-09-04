class Solution(object):
    def lengthOfLongestSubstring(self, s):
        index = 0
        arr = []
        k = 0

        while index < len(s):
            dic = {}
            arr.append("")
            for i in s[index:]:
                if i not in dic:
                    arr[k] += i
                    dic[i] = "p"
                else:
                    break
            index += 1
            k += 1
        fin = 0
        for i in arr:
            if len(i) > fin:
                fin = len(i)
        return fin