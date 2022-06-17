#include <iostream>
#include <vector>

using namespace std;

int a[100][100];
int y, x; // y =h , x= w
int n;

int feed_y, feed_x;
int ant_y, ant_x;

int b[11][11];
vector <int> v;
void sol1() {

	cin >> x >> y;

	cin >> n;

	for (int i = 0; i < n; i++) {

		int t_x, t_y;
		int r_x, r_y;
		int l, d;
		cin >> l >> d >> t_x >> t_y;

		r_x = t_x - 1;
		r_y = t_y - 1;

		if (d == 0) {
			for (int j = 0; j < l; j++)
			{
				a[r_x][r_y + j] = 1;

			}


		}


		else {
			for (int i = 0; i <l; i++)
			{
				a[r_x + i][r_y] = 1;
			}
		}


	}


	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			cout << a[i][j] << " ";

		}
		cout << "\n";
	}


}

void sol2() {

	for (int i = 1; i <= 10;i++)
	{
		for (int j = 1; j <= 10;j++)
		{
			int temp;
			cin >> temp;
			b[i][j] = temp;
			if (temp == 2) {
				feed_y = i;
				feed_x = j;

			}
		}
	}

	ant_y = 2;
	ant_x = 2;


	while (1)
	{

		if (b[ant_y][ant_x] == 0) {
			b[ant_y][ant_x] = 9;
			ant_x++;
			
		}

		if (b[ant_y][ant_x] == 1)
		{
			ant_x--;
			ant_y++;
		}

		if (b[ant_y][ant_x] == 2)
		{
			b[ant_y][ant_x] = 9;
			break;
		}

		else if (b[ant_y][ant_x+1] ==1 && b[ant_y+1][ant_x]==1){

			if (b[ant_y][ant_x] == 0) {
				b[ant_y][ant_x] = 9;
			}
			break;
			
		}
	}
	for (int i = 1; i <= 10; i++)
	{
		for (int j = 1; j <= 10; j++)
		{
			cout << b[i][j] << " ";
		}
		cout << "\n";
	}

}
int main() {

	//sol1();
	sol2();

}
