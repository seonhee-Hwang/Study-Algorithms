#include <iostream>
using namespace std;

int main()
{
    // 2차원 배열 a 선언
    int a[10][10] = { 0, };

    // 상자의 구조를 입력 받는다.
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            int t = 0;
            cin >> t;
            a[i][j] = t;
        }
        //cout << endl;
    }

    // 개미를 이동 시킨다.
    int x = 1;
    int y = 1;

    while (1) {

        // 시작점이 2이면 끝낸다.
        if (a[1][1] == 2) {
            a[1][1] = 9;
            break;
        }
        // 시작점이 2가 아니면 9로 바꾼다.
        else { a[1][1] = 9; }

        // 오른쪽으로 갈 수 있다면 오른쪽으로 이동한다.
        if (a[x][y + 1] == 0) {
            a[x][y + 1] = 9;
            y += 1;
        }
        // 오른쪽으로 갈 수 없다면 아래를 탐색해본다.
        else if (a[x][y + 1] == 1) {
            // 아래로 갈 수 있을 때
            if (a[x + 1][y] == 0) {
                a[x + 1][y] = 9;
                x += 1;
            }
            // 아래에 길이 막혔을 때
            else if (a[x + 1][y] == 1) {
                break;
            }
            // 아래에 먹이가 있을 때
            else if (a[x + 1][y] == 2) {
                a[x + 1][y] = 9;
                break;
            }
            else { break; }
        }
        else if (a[x][y + 1] == 2) {
            a[x][y + 1] = 9;
            break;
        }
        else { break; }
    }

    //cout << endl << endl;
    // 출력한다.
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cout << a[i][j];
            cout << " ";
        }
        //cout << endl;
        cout << endl;
    }

    return 0;
}