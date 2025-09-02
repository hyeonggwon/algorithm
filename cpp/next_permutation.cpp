#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    vector<int> v = {3, 2, 1};

    // 순열을 사용하기 전에는 데이터가 모두 사전순으로 정렬된 상태여야 한다.
    sort(v.begin(), v.end());

    // 시간복잡도 : O(n * n!)
    do {
        for (int i : v) {
            cout << i << " ";
        }
        cout << endl;
    } while (next_permutation(v.begin(), v.end()));
    return 0;
}