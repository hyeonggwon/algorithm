#include<vector>
#include<algorithm>

using namespace std;

// 수도 코드

/*
stages 돌면서 각 스테이지의 도전자와 실패 수를 각각 배열로 저장
도전자와 실패 수 배열을 이용해 (스테이지 번호, 실패율) 배열 생성
(스테이지 번호, 실패율) 배열을 실패율에 대해 내림차순, 스테이지 번호에 대해 오름차순으로 정렬 
스테이지 번호만 배열로 뽑아낸 후 리턴
*/

bool compare(pair<int, float>& a, pair<int, float>& b) {
    return a.second > b.second || (a.second == b.second && a.first < b.first);
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<float> challenger(N + 2, 0.0);
    vector<float> fail(N + 2, 0.0);
    
    for (int i = 0; i < stages.size(); ++i) {
        for (int j = 1; j <= stages[i]; ++j) {
            challenger[j]++;
        }
        fail[stages[i]]++;
    }

    vector<pair<int, float>> failRatio(N);
    for (int i = 0; i < N; ++i) {
        failRatio[i].first = i + 1;

        if (challenger[i + 1] == 0) {
            failRatio[i].second = 0;
        } else {
            failRatio[i].second = fail[i + 1] / challenger[i + 1];
        }
    }

    sort(failRatio.begin(), failRatio.end(), compare);
    for (auto &pair : failRatio) {
        answer.push_back(pair.first);
    }
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
    print(solution(5, {2, 1, 2, 6, 2, 4, 3, 3})); // 3 4 2 1 5
    print(solution(4, {4, 4, 4, 4, 4}));          // 4 1 2 3 
    print(solution(1, {1, 2, 1, 2, 1}));          // 4 1 2 3 

    return 0;
}