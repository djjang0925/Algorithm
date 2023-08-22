#include <iostream>

using namespace std;

int blackjack(int input, int max) {
	int arr[input];
	int min = 0;
	int sum = max;
	int temp;

	for(int i = 0; i < input; i++) {
		int num;

		cin >> num;

		arr[i] = num;
	}

	for(int i = 0; i < (input - 2); i++) {
		for(int j = (i + 1); j < (input - 1); j++){
			for(int k = (j + 1); k < input; k++) {	
				temp = arr[i] + arr[j] + arr[k];
				
				if(temp == max) {
					return temp;
				}

				else if((temp > min) && (temp < max)) {
					sum = temp;
					min = temp;
				}
			}
		}
	}
	
	return sum;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int input, max;

	cin >> input >> max;

	cout << blackjack(input, max) << '\n';

	return 0;
}
