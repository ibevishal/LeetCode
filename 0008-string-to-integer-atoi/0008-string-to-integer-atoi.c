int myAtoi(char* s) {
    long long num = 0;
    int sign = 1;
    int i = 0;
    int digit;

    while (s[i] == ' ') {
        i++;
    }

    if (s[i] == '-') {
        sign = -1;
        i++;
    }
    else if (s[i] == '+') {
        i++;
    }

    while (s[i] != '\0') {

        if (s[i] == '0')
            digit = 0;
        else if (s[i] == '1')
            digit = 1;
        else if (s[i] == '2')
            digit = 2;
        else if (s[i] == '3')
            digit = 3;
        else if (s[i] == '4')
            digit = 4;
        else if (s[i] == '5')
            digit = 5;
        else if (s[i] == '6')
            digit = 6;
        else if (s[i] == '7')
            digit = 7;
        else if (s[i] == '8')
            digit = 8;
        else if (s[i] == '9')
            digit = 9;
        else
            break;

        num = num * 10 + digit;

        if (sign == 1 && num > 2147483647)
            return 2147483647;

        if (sign == -1 && num > 2147483648LL)
            return -2147483648LL;

        i++;
    }

    return sign * num;
}