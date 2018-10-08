#include <iostream>
#include <algorithm>

using namespace std;
#define INF 100000
#define FOR(i, a, b) for(int(i) = (a); (i) <= (b); (i)++)

int main() {
    int coins[3] = {1, 3, 4};
    int M;
    cin >> M;
    int C[M + 1] = {0};
    FOR(i, 1, M) {
        int ans = INF;
        FOR(k, 0, 2) {
            if (i >= coins[k]) {
                ans = min(ans, 1 + C[i - coins[k]]);
            }
        }
        C[i] = ans;
    }
    cout << C[M];
    return 0;
}

