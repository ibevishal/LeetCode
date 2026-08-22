class Solution(object):
    def topKFrequent(self, nums, k):

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        arr = []
        j = 1

        for i in dic:
            arr.append(i[0])

            if j == k:
                break

            j += 1

        return arr