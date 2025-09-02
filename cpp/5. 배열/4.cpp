#include<vector>
#include<algorithm>

using namespace std;

// 내 풀이 : 배열 사용했으나, vector 써서 size랑 max_element 사용하는 게 더 효율적. 답안 참고.
vector<int> solution(vector<int> answers) {
    int answer1[5] = {1, 2, 3, 4, 5};
    int answer2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int answer3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    int cnt[3] = {};

    for (int i = 0; i < answers.size(); ++i) {
        if (answers[i] == answer1[i % 5])
            ++cnt[0];
        if (answers[i] == answer2[i % 8])
            ++cnt[1];
        if (answers[i] == answer3[i % 10])
            ++cnt[2];
    }

    vector<int> result;
    int maxCnt = -1;
    for (int i = 0; i < 3; ++i)
        if (maxCnt < cnt[i])
            maxCnt = cnt[i];

    for (int i = 0; i < 3; ++i)
        if (maxCnt == cnt[i])
            result.push_back(i + 1);
    
    return result;
}

// 답안
vector<int> firstPattern = {1, 2, 3, 4, 5};
vector<int> secondPattern = {2, 1, 2, 3, 2, 4, 2, 5};
vector<int> thirdPattern = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> matchCnt(3);
    for (int i = 0; i < answers.size(); ++i) {
        if (answers[i] == firstPattern[i % firstPattern.size()])
            matchCnt[0]++;
        if (answers[i] == secondPattern[i % secondPattern.size()])
            matchCnt[1]++;
        if (answers[i] == thirdPattern[i % thirdPattern.size()])
            matchCnt[2]++;
    }

    int max_score = *max_element(matchCnt.begin(), matchCnt.end());

    for (int i = 0; i < 3; ++i) {
        if (matchCnt[i] == max_score)
            answer.push_back(i + 1);
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
    print(solution({1, 2, 3, 4, 5}));     // 1 
    print(solution({1, 3, 2, 4, 2}));     // 1 2 3 
    print(solution({2, 1, 2, 2}));     // 2
    
    return 0;
}