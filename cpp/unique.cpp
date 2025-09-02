#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    vector<int> v = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5};

    // 시간복잡도 : O(n)
    // unique는 중복된 요소를 뒤에 남겨두고, 새로운 끝을 반환한다.
    auto newEnd = unique(v.begin(), v.end());

    cout << "Unique elements: ";
    for (auto it = v.begin(); it != newEnd; ++it) {
        cout << *it << " ";
    }
    cout << endl;

    cout << "Total elements: ";
    for (auto it = v.begin(); it != v.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}