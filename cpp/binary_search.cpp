#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    // binray_search는 정렬된 컨테이너에서만 사용할 수 있다.
    // 정렬되지 않은 컨테이너를 정렬해서 binary_search를 사용하면 선형 탐색보다 오히려 더 비효율적이다.
    vector<int> v = {1, 2, 3, 4, 5};
    cout << binary_search(v.begin(), v.end(), 3) << endl;
    cout << binary_search(v.begin(), v.end(), 7) << endl;

    return 0;
}    