#include <iostream>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)

int Max(int a, int b, int c, int d, int e, int f, int g)  {
    return max(max(max(a,b), max(c, d)), max(max(e, f), g));
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

    int L3;
    cin >> L3;
    int S3[L3] = {0};
    FOR(i, 0, L3 - 1) {
        cin >> S3[i];
    }

    int Match[L1 + 1][L2 + 1][L3 + 1];

    FOR (i, 0, L1) {
        FOR(j, 0, L2) {
            FOR(k, 0, L3)
                Match[i][j][k] = 0;
        }
    }

    bool M1[L1] = {0};
    bool M2[L2] = {0};
    bool M3[L3] = {0};
    FOR(i, 1, L1) {
        FOR(j, 1, L2) {
            FOR(k, 1, L3){
                Match[i][j][k] = Max(Match[i - 1][j][k], Match[i - 1][j - 1][k], Match[i - 1][j][k - 1], Match[i][j - 1][k], Match[i][j - 1][k - 1], Match[i][j][k - 1], Match[i - 1][j - 1][k - 1]);
                if ((S1[i - 1] == S2[j - 1] && S1[i - 1] == S3[k - 1]) && M1[i - 1] == 0 && M2[j - 1] == 0 && M3[k - 1] == 0){
                    M1[i - 1] = 1;
                    M2[j - 1] = 1;
                    M3[k - 1] = 1;
                    Match[i][j][k] += 1;
                }

            }
        }
    }

    cout << Match[L1][L2][L3];
}
