#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct Point {
    int x, y;

    Point(int x, int y) : x(x), y(y) {}
};

bool compare(const Point& a, const Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

int main() {
    vector<int> v = {4, 2, 5, 3, 1};

    // 시간복잡도 : O(nlogn)
    sort(v.begin(), v.end());
    
    cout << "Sorted vector: ";
    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;

    sort(v.rbegin(), v.rend());
    cout << "Sorted vector: ";
    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;

    vector<Point> points = {{3, 4}, {1, 2}, {3, 1}, {2, 5}};

    sort(points.begin(), points.end(), compare);

    cout << "Sorted vector: ";
    for (const auto& p : points) {
        cout << "(" << p.x << ", " << p.y << ") ";
    }
    cout << endl;

    sort(points.rbegin(), points.rend(), compare);

    cout << "Sorted vector: ";
    for (const auto& p : points) {
        cout << "(" << p.x << ", " << p.y << ") ";
    }
    cout << endl;

    return 0;
}