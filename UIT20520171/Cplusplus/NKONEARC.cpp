#include <cmath>
#include <iostream>
#include <vector>

using namespace std;
int main()
{

	int soMay, soKenh, mayBiTanCong;
	// Nhập 
	cin >> soMay >> soKenh;
    
    int **ketNoi = new int*[soKenh];
    int *danhSach = new int[soKenh];
    
	for (int i = 0; i < soKenh; i++) {
		ketNoi[i] = new int[2];
		cin >> ketNoi[i][1];
		cin >> ketNoi[i][0];
	}
	
	cin >> mayBiTanCong;

	// Chạy chương trình
	int duplicate;
	int count = 1;
	danhSach[0] = mayBiTanCong;
	for (int i = 0; i < soKenh; i++)
	{
		for (int i2 = 0; i2 < count; i2++)
		{ 
			int temp = danhSach[i2];
			
			if (temp == ketNoi[i][0])
			{
				duplicate = 0;
				for (int i3 = 0; i3 < count; i3++)
					if (danhSach[i3] == ketNoi[i][1])
						duplicate = 1;
				if (duplicate == 0)
				{
					danhSach[count++] = ketNoi[i][1];
				}
			}
			if (temp == ketNoi[i][1])
			{
				duplicate = 0;
				for (int i3 = 0; i3 < count; i3++)
					if (danhSach[i3] == ketNoi[i][0])
						duplicate = 1;
				if (duplicate == 0)
				{
					danhSach[count++] = ketNoi[i][0];
				}
			}
		}
	}

	for (int i = 0; i < count - 1; i++)
	{
		int min = i;
		for (int j = i + 1; j < count; j++)
			if (danhSach[min] > danhSach[j])
				min = j;
		swap(danhSach[i], danhSach[min]);
	}

	// Xuất
	cout<< count <<endl;
	for (int i = 0; i < count; i++)
		cout << danhSach[i] << " ";
	
	return 0;
}