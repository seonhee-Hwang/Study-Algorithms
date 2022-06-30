#include <iostream>
using namespace std;


// int형 2차워 배열 동적 할당하는 함수
int** alloc2Darr(int w, int h) {
    if (w <= 0 || h <= 0) return NULL;
    int** a = new int* [h];
    for (int i = 0; i < h; i++) {
        a[i] = new int[w];
    }
    return a;
}

// int형 2차원 배열 동적 할당 해제하는 함수
void free2DArr(int** a, int w, int h = 0) {
    if (a != NULL) {
        for (int i = 0; i < h; i++)
            delete[] a[i];
        delete[] a;
    }
}

int main()
{
    // 가로 w, 세로 h를 입력 받는다.
    int h, w = 0;
    cin >> h >> w;

    // 2차원 배열 a 선언
    int** a;
    // 2차원 배열 a 할당
    a = alloc2Darr(w, h);


    //for (int i = 0; i < h; i++)
    //{
    //    for (int j = 0; j < w; j++)
    //    {
    //        a[i][j] = 0;
    //        cout << a[i][j];
    //    }
    //    cout << endl;
    //}

    // 막대 개수를 입력 받는다.
    int n = 0;
    cin >> n;


    // 각 막대의 정보를 입력 받는다.
    for (int k = 1; k <= n; k++) {
        int l, d, x, y = 0;
        cin >> l >> d >> x >> y;

        x = x - 1;
        y = y - 1;

        // d가 0이면 가로로 눕히므로 h가 고정
        if (d == 0) {
            for (int i = 0; i < l; i++) {
                a[x][y + i] = 1;
            }
        }
        // d가 1이면 세로로 눕히므로 w가 고정
        else {
            for (int i = 0; i < l; i++) {
                a[x + i][y] = 1;
            }
        }
    }

    // 출력한다.
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << a[i][j];
            cout << " ";
        }
        cout << endl;
    }

    // 2차원 배열 a 할당 해제
    free2DArr(a, w, h);

    return 0;
}