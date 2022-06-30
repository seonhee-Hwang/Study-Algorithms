#include <iostream>
using namespace std;

int main()
{
    //2차원 배열로 입력을 받는다.
    int a[20][20];
    for (int i = 1; i <= 19; i++) {
        for (int j = 1; j <= 19; j++) {
            cin >> a[i][j];
        }
    }

    // 좌표 개수를 입력 받는다.
    int n = 0;
    cin >> n;

    // 좌표를 입력 받는다.
    for (int k = 1; k <= n; k++) {
        int x, y = 0;
        cin >> x;
        cin >> y;
        for (int i = 1; i <= 19; i++) {
            if (a[x][i] == 0) { a[x][i] = 1; }
            else { a[x][i] = 0; }
        }
        for (int i = 1; i <= 19; i++) {
            if (a[i][y] == 0) { a[i][y] = 1; }
            else { a[i][y] = 0; }
        }

    }

    // 출력한다.
    for (int i = 1; i <= 19; i++) {
        for (int j = 1; j <= 19; j++) {
            cout << a[i][j];
            cout << " ";
        }
        cout << endl;
    }
}