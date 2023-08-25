#include <iostream>
#include <vector>

using namespace std;

int main() {
	
	vector<double> v;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> fixed;
	cout.precision(3);

	int input;
	cin >> input;

	while(input--) {
		int count = 0;
		int avg = 0;
		int t;
		cin >> t;
		v.clear();

		for(int i = 0; i < t; i++) {
			int tt;
			cin >> tt;
			v.push_back(tt);
			avg += tt;
		}

		avg /= t;

		for(int i : v) {
			if(i > avg) {
				count++;
			}
		}

		cout << (double)count / (double)t * 100 << "%\n";
	}

	return 0;
}
