class Solution:
    def romanToInt(self, s: str) -> int:
        su=0
        i=0
        while i< len(s)-1:
            if s[i]=="I":
                if s[i+1]=="V":
                    su+=4
                    i+=2
                elif s[i+1]=="X":
                    su+=9
                    i+=2
                else:
                    su+=1
                    i+=1
            elif s[i]=="X":
                if s[i+1]=="L":
                    su+=40
                    i+=2
                elif s[i+1]=="C":
                    su+=90
                    i+=2
                else:
                    su+=10
                    i+=1
            elif s[i]=="C":
                if s[i+1]=="D":
                    su+=400
                    i+=2
                elif s[i+1]=="M":
                    su+=900
                    i+=2
                else:
                    su+=100
                    i+=1
            elif s[i]=="V":
                su+=5
                i+=1
            elif s[i]=="L":
                su+=50
                i+=1
            elif s[i]=="D":
                su+=500
                i+=1
            elif s[i]=="M":
                su+=1000
                i+=1
        if i < len(s):
            if s[i] == "I":
                su += 1
            elif s[i] == "V":
                su += 5
            elif s[i] == "X":
                su += 10
            elif s[i] == "L":
                su += 50
            elif s[i] == "C":
                su += 100
            elif s[i] == "D":
                su += 500
            elif s[i] == "M":
                su += 1000
        return su