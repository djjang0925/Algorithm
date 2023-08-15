#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;

int center(int num) {
	int start = 0;
	int end = arr.size() - 1;
	int mid;

	while(start <= end) {
		mid = (start + end) / 2;

		if(arr[mid] < num) {
			start = mid + 1;
		}

		else if(arr[mid] > num) {
			end = mid - 1;
		}

		else {
			return 1;
		}
	}

	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int input;

	cin >> input;

	for(int i = 0; i < input; i++) {
		int num;

		cin >> num;

		arr.push_back(num);
	}
	
	sort(arr.begin(), arr.end());

	int test;

	cin >> test;
	
	for(int i = 0; i < test; i++) {
		int num;

		cin >> num;

		cout << center(num) << '\n';
	}

	return 0;
}
