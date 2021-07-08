#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int soMay, soKenh, mayBiTanCong, ketNoi[10000][2];
    int danhSach[10000], duplicate, Count = 1, temp;
    
	cin >> soMay >> soKenh;
	for (int i = 0; i < soKenh; i++) {
		cin >> ketNoi[i][1];
		cin >> ketNoi[i][0];
	}
	cin >> mayBiTanCong;


	danhSach[0] = mayBiTanCong;
	for (int i = 0; i < soKenh; i++)
	{
		for (int i2 = 0; i2 < Count; i2++)
		{
			temp = danhSach[i2];
			if (temp == ketNoi[i][0])
			{
				duplicate = 0;
				for (int i3 = 0; i3 < Count; i3++)
					if (danhSach[i3] == ketNoi[i][1])
						duplicate = 1;
				if (duplicate == 0)
				{
					danhSach[Count++] = ketNoi[i][1];
				}
			}
			if (temp == ketNoi[i][1])
			{
				duplicate = 0;
				for (int i3 = 0; i3 < Count; i3++)
					if (danhSach[i3] == ketNoi[i][0])
						duplicate = 1;
				if (duplicate == 0)
				{
					danhSach[Count++] = ketNoi[i][0];
				}
			}
		}
	}

	for (int i = 0; i < Count - 1; i++)
	{
		int min = i;
		for (int j = i + 1; j < Count; j++)
			if (danhSach[min] > danhSach[j])
				min = j;
		swap(danhSach[i], danhSach[min]);
	}

	cout<< Count <<endl;
	for (int i = 0; i < Count; i++)
		cout << danhSach[i]<<" ";
    return 0;
}