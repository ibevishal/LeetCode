class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def su(j, k, c):
            j, k = int(j), int(k)
            
            total = j + k + c
            if total == 0:   return 0, "0"
            elif total == 1: return 0, "1"
            elif total == 2: return 1, "0"
            elif total == 3: return 1, "1"
        la=len(a)
        lb=len(b)

        if la>lb:
            n=la-lb
            for i in range(n):
                b="0"+ b
        if lb>la:
            n=lb-la
            for i in range(n):
                a="0"+a
        suu=""
        c=0
        for i in range(len(a)-1,-1,-1):
            c,k=su(a[i],b[i],c)
            suu+=k
        if c==1:
            suu+=str(c)
        return suu[::-1]
        