#include<iostream>
#include<vector>

using namespace std;

double get_avg(const vector<int>& arr, int N) {
    if (arr.empty()) {
        return -1; // Return -1 for empty array
    }

    if (N <= 0) {
        return -1; // Return -1 for invalid size
    }

    int sum = 0;
    for (int num : arr) {
        sum += num;
    }
    return sum;
}

int main() {
    vector<int> empty_arr;
    vector<int> arr = {1, 2, 3, 4, 5};

    cout << "Average of empty array: " << get_avg(empty_arr, 0) << endl; // Should return -1
    cout << "Average of array: " << get_avg(arr, arr.size()) << endl; // Should return 15
    return 0;
}