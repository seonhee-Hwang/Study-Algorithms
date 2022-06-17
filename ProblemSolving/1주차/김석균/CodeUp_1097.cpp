#include <iostream>

using namespace std;

int a[20][20];

int N;

int main() {

	for (int i = 1; i <= 19; i++)
	{
		for (int j = 1; j <= 19; j++)

		{
			int temp;
			cin >> temp;
			a[i][j] = temp;

		}
	}

	cin >> N;

	for (int i = 0; i < N;i++)
	{
		int x, y;
		cin >> x >> y;
		bool t[20][20];
		for (int i = 1; i <= 19; i++)
		{
			if (a[i][y] == 0) {
				a[i][y] = 1;
				//t[i][y] = true;
			}

			else {
				a[i][y] = 0;
				//t[i][y] = true;
			}
		}

		for (int j = 1; j <= 19; j++)
		{
			if (a[x][j] == 0 ) { a[x][j] = 1; }

			else if (a[x][j] ==1 ) { a[x][j] = 0; }

		}


	}



	for (int i = 1; i <= 19;i++) {
	
		for (int j = 1; j <= 19;j++)
		{
			cout << a[i][j] << " ";

		}

		cout << "\n";
	}
}