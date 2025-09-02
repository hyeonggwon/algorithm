#include<vector>
#include<algorithm>
#include<set>

using namespace std;
// 내 풀이 : 시간복잡도 O(n) 이지만 메모리 더 사용
vector<int> solution(vector<int> lst) {
    set<int> unique_vec = set<int>(lst.begin(), lst.end());
    return vector<int>(unique_vec.rbegin(), unique_vec.rend());
}

// 답안지 : 시간복잡도 O(nlogn) 이지만 메모리 덜 사용
bool compare(int a, int b) {
    return a > b;
}

vector<int> solution(vector<int> lst) {
    sort(lst.begin(), lst.end(), compare);
    lst.erase(unique(lst.begin(), lst.end()), lst.end());
    return lst;
}

//아래 코드는 테스트 코드 입니다.
#include <iostream>
#include <iterator>
void print(vector<int> vec)
{
    copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
    cout << endl;
}

int main()
{
    print(solution({4, 2, 2, 1, 1, 3, 4})); // 4 3 2 1  
    print(solution({2, 1, 1, 3, 2, 5, 4})); // 5 4 3 2 1
    
    return 0;
}