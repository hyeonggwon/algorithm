#include<unordered_set>
#include<iostream>

using namespace std;

int main() {
    unordered_set<int> uset = {1, 2, 3, 4, 5};

    // 시간복잡도 : O(1)
    auto it = uset.find(3);
    if (it != uset.end()) {
        cout << *it << endl;
    }

    // 시간복잡도 : O(1)
    uset.insert(6);
    uset.insert(7);

    cout << "Unordered set: ";
    for (int i : uset) {
        cout << i << " ";
    }
    cout << endl;

    uset.erase(3);
    cout << "Unordered set after erasing 3: ";
    for (int i : uset) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}