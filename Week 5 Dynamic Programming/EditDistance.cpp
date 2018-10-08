#include <iostream>
#include <string>
using namespace std;

#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)

int Min(int a, int b, int c) {
    if (a <= b && a <= c)
        return a;
    if (b <= a && b <= c)
        return b;
    if (c <= a && c <= b)
        return c;
}
int main() {
    string S1;
    string S2;

    cin >> S1;
    cin >> S2;

    int len1 = S1.length();
    int len2 = S2.length();

    int ED[len1 + 1][len2 + 1] = {{0,0}};

    FOR (i, 0, len1) {
        ED[i][0] = i;
    }
    FOR (i, 0, len2) {
        ED[0][i] = i;
    }


    FOR (i, 1 , len1){
        FOR(j, 1, len2) {
            int inse = ED[i][j - 1] + 1;
            int dele = ED[i - 1][j] + 1;
            int mism = ED[i - 1][j - 1] + 1;
            int matc = ED[i - 1][j - 1];

            if (S1[i - 1] == S2[j - 1]) {
                ED[i][j] = Min(inse, dele, matc);
            }
            else
                ED[i][j] = Min(inse, dele, mism);
        }
    }

    cout << ED[len1][len2];
    return 0;

}

