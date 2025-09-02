#include<vector>
#include<algorithm>
#include<set>

using namespace std;

// 내 풀이 : 시간복잡도 O(n^2), 근데 it 안 쓰고 그냥 인덱스로 해도 됨. 답안 참고
vector<int> solution(vector<int> numbers) {
    vector<int> result;
    for (auto it1 = numbers.begin(); it1 != numbers.end(); ++it1) {
        for (auto it2 = it1 + 1; it2 != numbers.end(); ++it2) {
            if (it1 != it2) {
                result.push_back(*it1 + *it2);
            }
        }
    }
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}

// 답안 : 시간복잡도 O(n^2logn)
vector<int> solution(vector<int> numbers) {
    set<int> sum;

    for (int i = 0; i < numbers.size(); ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            sum.insert(numbers[i] + numbers[j]);
        }
    }

    vector<int> answer(sum.begin(), sum.end());
    return answer;
}

//아래 코드는 테스트 코드 입니다.

#include <iterator>
#include <iostream>
void print(vector<int> vec)
{
    copy(vec.begin(), vec.end(), std::ostream_iterator<int>(cout, " "));
    cout << endl;
}

int main()
{
    print(solution({2, 1, 3, 4, 1}));     // 2 3 4 5 6 7 
    print(solution({5, 0, 2, 7}));        // 2 5 7 9 12 
    
    return 0;
}