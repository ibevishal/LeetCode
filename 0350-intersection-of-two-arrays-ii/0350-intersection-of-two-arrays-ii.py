class Solution(object):
    def intersect(self, nums1, nums2):
        dic = {}
        arr = []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums2:
            if i in dic and dic[i] > 0:
                arr.append(i)
                dic[i] -= 1
        return arr