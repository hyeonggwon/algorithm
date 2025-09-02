#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    vector<int> v = {1, 3, 5, 7, 2, 4, 6};
    
    // 시간복잡도 : O(n)
    auto maxInt = max_element(v.begin(), v.end());
    auto minInt = min_element(v.begin(), v.end());

    cout << *maxInt << endl;
    cout << *minInt << endl;

    return 0;
}