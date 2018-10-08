#include <iostream>
#include <algorithm>
using namespace std;
#define INF 10000000
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)

int Min (int a, int b, int c) {
    if (a <= b && a <= c)
        return a;
    if (b <= a && b <= c)
        return b;
    if (c <= a && c <= b)
        return c;
}

void printInter(int num, int A[]) {
    if (num == 1) {
        cout << 1 << " ";
        return ;
    }

    int a;
    int c = INF;
    int b = INF;
    a = A[(num - 1) - 1];
    if (num % 2 == 0) {
        b = A[(num / 2) - 1];
    }
    if (num % 3 == 0) {
        c = A[(num / 3) - 1];
    }

    if (Min(a, b, c) == a) {
        printInter(num - 1, A);
    }
    else if (Min(a, b, c) == b) {
        printInter((num / 2), A);
    }
    else {
        printInter((num / 3), A);
    }
    cout << num << " ";
}

int main() {
    int n;
    cin >> n;

    if (n == 1) {
        cout << 0 << endl;
        cout << 1;
    }
    else {
        int A[n] = {INF};
        A[0] = 0;

        FOR (i, 1, n - 1) {
            int ans = INF;
            ans = min(ans, 1 + A[i - 1]);
            if ((i + 1) % 2 == 0)
                ans = min(ans, 1 + A[((i + 1) / 2) - 1]);
            if ((i + 1) % 3 == 0)
                ans = min(ans, 1 + A[((i + 1) / 3) - 1]);
            A[i] = ans;
        }


        cout << A[n - 1] << endl;

        printInter(n,A);

    }
    return 0;
}
