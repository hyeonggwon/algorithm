// 내 풀이 (답안이 더 깔끔함)
// 수도코드
/*
현재 좌표 변수 생성, 모든 경로 담은 unordered_set 생성. 모든 경로는 vector<pair<int, int>> 이며 이 벡터는 정렬되어 있어야 함
dir 움직일 때 마다 현재 좌표 변경, 움직일 때 마다 unordered_set에 경로 추가
모두 다 움직였으면, unordered_set의 크기 리턴
*/
// #include <unordered_set>
// #include <vector>
// #include <algorithm>
// #include <utility>
// #include <functional>

// using namespace std;

// struct VectorPairHash {
//     size_t operator()(const vector<pair<int, int>>& vec) const {
//         size_t _hash = 0;
//         for (const auto& p : vec) {
//             _hash ^= hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
//         }
//         return _hash;
//     }
// };

// struct VectorPairEqual {
//     bool operator()(const vector<pair<int, int>>& a, const vector<pair<int, int>>& b) const {
//         return a == b;
//     }
// };

// int solution(string dirs) {
//     unordered_set<vector<pair<int, int>>, VectorPairHash, VectorPairEqual> allPaths;
//     vector<pair<int, int>> path;
//     pair<int, int> currentPoint = {0 , 0};
//     pair<int, int> nextPoint;
//     for (char c : dirs) {
//         switch(c) {
//             case 'L':
//             if (currentPoint.first == -5)
//                 break;
//             nextPoint = {currentPoint.first - 1, currentPoint.second};
//             break;

//             case 'R':
//             if (currentPoint.first == 5)
//                 break;
//             nextPoint = {currentPoint.first + 1, currentPoint.second};
//             break;

//             case 'D':
//             if (currentPoint.second == -5)
//                 break;
//             nextPoint = {currentPoint.first, currentPoint.second - 1};
//             break;

//             case 'U':
//             if (currentPoint.second == 5)
//                 break;
//             nextPoint = {currentPoint.first, currentPoint.second + 1};
//             break;

//             default:
//             break;
//         }

//         if (nextPoint != currentPoint) {
//             path.push_back(currentPoint);
//             path.push_back(nextPoint);
//             sort(path.begin(), path.end());
//             allPaths.insert(path);
//             currentPoint = nextPoint;
//             path = {};
//         }
//     }

//     return allPaths.size();
// }

// 답안
// 수도 코드
/*
visited 배열 생성 : [y][x][dir], 좌표는 원점을 (0, 0)이 아닌 (5, 5)로 설정
방향별로 가중치를 정의한 dx, dy 생성
'U', 'R', 'D', 'L' 별 인덱스로 리턴하는 함수 생성
다음 좌표의 이상여부를 체크하는 함수 생성
반대 방향 인덱스를 리턴하는 함수 생성
경로 개수 answer 변수 생성
dirs을 돌면서, 문자를 인덱스로 변경 한다. 해당 인덱스로 현재 좌표에 가중치를 더하여 다음 좌표 계산
다음 좌표가 이상하면 continue 한다
현재 좌표와 방향이 visited 되지 않았으면, 현재 방향과 반대방향 모두 visited true 설정 후 현재 좌표 다음 좌표로 설정, answer++
반복문 나와서 answer 리턴
*/
#include <iostream>

using namespace std;

int visited[11][11][4];

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int todir(char dir) {
    int ret;
    if (dir == 'U')
        ret = 0;
    else if (dir == 'R')
        ret = 1;
    else if (dir == 'D')
        ret = 2;
    else
        ret = 3;
    return ret;
}

bool isNotValid(int x, int y) { return x < 0 || y < 0 || x > 10 || y > 10; }
int opposite_direction(int dir) { return (dir + 2) % 4; }

int solution(string dirs) {
    int answer = 0;
    int x = 5, y = 5;

    for (auto c : dirs) {
        int dir = todir(c);
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (isNotValid(nx, ny))
            continue;
        
        if (!visited[y][x][dir]) {
            visited[y][x][dir] = true;
            visited[ny][nx][opposite_direction(dir)] = true;
            answer++;
        }
        x = nx;
        y = ny;
    }

    return answer;
}

//아래 코드는 테스트 코드 입니다.

int main()
{
    cout << solution("ULURRDLLU") << endl; // 7
    cout << solution("LULLLLLLU") << endl; // 7 

    return 0;
}