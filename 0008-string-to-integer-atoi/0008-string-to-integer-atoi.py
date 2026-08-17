class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        a = 0

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1

        while i < len(s):
            if s[i] == '0':
                digit = 0
            elif s[i] == '1':
                digit = 1
            elif s[i] == '2':
                digit = 2
            elif s[i] == '3':
                digit = 3
            elif s[i] == '4':
                digit = 4
            elif s[i] == '5':
                digit = 5
            elif s[i] == '6':
                digit = 6
            elif s[i] == '7':
                digit = 7
            elif s[i] == '8':
                digit = 8
            elif s[i] == '9':
                digit = 9
            else:
                break

            num = num * 10 + digit
            i += 1

        num *= sign

        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648

        return num