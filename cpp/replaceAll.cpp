#include<iostream>
#include<string>

// 시간복잡도 : O(n)
std::string replaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
    return str;
}

int main() {
    std::string str = "Hello, Hello, World, Hello!";
    str = replaceAll(str, "Hello", "Hi");
    std::cout << str << std::endl;
}