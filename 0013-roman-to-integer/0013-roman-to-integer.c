int romanToInt(char* s) {
    int su = 0;
    int i = 0;

    while (i < strlen(s) - 1) {
        if (s[i] == 'I') {
            if (s[i + 1] == 'V') {
                su += 4;
                i += 2;
            }
            else if (s[i + 1] == 'X') {
                su += 9;
                i += 2;
            }
            else {
                su += 1;
                i += 1;
            }
        }

        else if (s[i] == 'X') {
            if (s[i + 1] == 'L') {
                su += 40;
                i += 2;
            }
            else if (s[i + 1] == 'C') {
                su += 90;
                i += 2;
            }
            else {
                su += 10;
                i += 1;
            }
        }

        else if (s[i] == 'C') {
            if (s[i + 1] == 'D') {
                su += 400;
                i += 2;
            }
            else if (s[i + 1] == 'M') {
                su += 900;
                i += 2;
            }
            else {
                su += 100;
                i += 1;
            }
        }

        else if (s[i] == 'V') {
            su += 5;
            i += 1;
        }

        else if (s[i] == 'L') {
            su += 50;
            i += 1;
        }

        else if (s[i] == 'D') {
            su += 500;
            i += 1;
        }

        else if (s[i] == 'M') {
            su += 1000;
            i += 1;
        }
    }

    if (i < strlen(s)) {
        if (s[i] == 'I')
            su += 1;
        else if (s[i] == 'V')
            su += 5;
        else if (s[i] == 'X')
            su += 10;
        else if (s[i] == 'L')
            su += 50;
        else if (s[i] == 'C')
            su += 100;
        else if (s[i] == 'D')
            su += 500;
        else if (s[i] == 'M')
            su += 1000;
    }

    return su;
}