#include <iostream>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)

int Max(int a, int b, int c)  {
    if (a >= b && a >= c)
        return a;
    if (b >= a && b >= c)
        return b;
    if (c >= a && c >= b)
        return c;
}

int main() {
    int L1;
    cin >> L1;

    int S1[L1] = {0};
    FOR(i, 0, L1 - 1) {
        cin >> S1[i];
    }

    int L2;
    cin >> L2;

    int S2[L2] = {0};
    FOR(i, 0, L2 - 1) {
        cin >> S2[i];
    }

    int Match[L1 + 1][L2 + 1];

    FOR (i, 0, L1) {
        FOR(j, 0, L2) {
            Match[i][j] = 0;
        }
    }

    bool M1[L1] = {0};
    bool M2[L2] = {0};
    FOR(i, 1, L1) {
        FOR(j, 1, L2) {
            Match[i][j] = Max(Match[i - 1][j], Match[i][j - 1], Match[i - 1][j - 1]);
            if (S1[i - 1] == S2[j - 1] && M1[i - 1] == 0 && M2[j - 1] == 0){
                M1[i - 1] = 1;
                M2[j - 1] = 1;
                Match[i][j] += 1;
            }
        }
    }

    cout << Match[L1][L2];
}
