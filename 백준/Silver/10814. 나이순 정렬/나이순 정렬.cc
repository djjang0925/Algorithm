#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	vector<string> member[201];

	int input;

	cin >> input;

	for(int i = 0; i < input; i++) {
		int age;
		string name;

		cin >> age >> name;

		member[age].push_back(name);
	}

	for(int i = 1; i < 201; i++) {
		for(int j = 0; j < member[i].size(); j++) {
			cout << i << ' ' << member[i][j] << '\n';
		}
	}

	return 0;
}
