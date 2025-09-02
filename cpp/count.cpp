#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    vector<int> v = {1, 4, 3, 4, 5, 4, 5};
    // 시간복잡도 : O(n)
    int ret = count(v.begin(), v.end(), 5);

    cout << ret << endl;

    return 0;
}