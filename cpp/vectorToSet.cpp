#include<iostream>
#include<vector>
#include<set>

int main() {
    std::vector<int> vec = {1, 2, 3, 3, 5};
    // 시간복잡도 : O(n)
    std::set<int> unique_vec(vec.begin(), vec.end());
    int targets[] = {3, 7};
    for (int target : targets) {
        auto it = unique_vec.find(target);
        if (it != unique_vec.end()) {
            std::cout << "Found: " << *it << std::endl;        
        } else {
            std::cout << "Not Found: " << target << std::endl;
        }
    }
}