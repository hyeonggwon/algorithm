#include <map>
#include <iostream>

using namespace std;

int main() {
    std::map<string, int> studentScores;

    // 시간복잡도 : O(logn)
    studentScores["Alice"] = 95;
    studentScores.insert({"Bob", 88});
    studentScores.insert(make_pair("Charlie", 92));

    int score1 = studentScores["Alice"];
    cout << score1 << endl;

    int score2 = studentScores["rabbit"];
    cout << score2 << endl;

    auto it = studentScores.find("Charlie");
    if (it != studentScores.end()) {
        int score3 = it->second;
        cout << score3 << endl;
    }
    
    cout << "\nAll students and scores:" << endl;
    for (const auto& pair : studentScores) {
        cout << pair.first << ": " << pair.second << endl;
    }

    studentScores.erase("Bob");
    cout << "\nAll students and scores:" << endl;
    for (const auto& pair : studentScores) {
        cout << pair.first << ": " << pair.second << endl;
    }

    it = studentScores.find("Charlie");
    if (it != studentScores.end()) {
        studentScores.erase(it);
    }

    cout << "\nAll students and scores:" << endl;
    for (const auto& pair : studentScores) {
        cout << pair.first << ": " << pair.second << endl;
    }
}