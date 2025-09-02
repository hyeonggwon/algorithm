#include<unordered_map>
#include<iostream>

int main() {
    std::unordered_map<std::string, int> umap;

    // 시간복잡도 : O(1)
    umap["Alice"] = 95;
    umap.insert({"Bob", 88});
    umap.insert(std::make_pair("Charlie", 92));

    std::cout << "Alice's score: " << umap["Alice"] << std::endl;
    std::cout << "Bob's score: " << umap["Bob"] << std::endl;

    // 시간복잡도 : O(1)
    auto it = umap.find("Charlie");
    if (it != umap.end()) {
        std::cout << "Charlie's score: " << it->second << std::endl;
    }

    // 시간복잡도 : O(1)
    umap.erase("Bob");
    
    std::cout << "\nAll students and scores:" << std::endl;
    for (const auto& pair : umap) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}