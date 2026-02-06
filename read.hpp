#ifndef SE_READ
#define SE_READ

#include <fstream>
#include <stdexcept>
#include <string>

#include <nlohmann/json.hpp>

namespace se {
nlohmann::json read(const std::string& path) {
    std::ifstream file(path);

    if (!file.is_open()) {
        throw std::runtime_error("文件损坏！");
    }
    
    std::string t;
    file.seekg(0, std::ios::end);
    t.resize(file.tellg());
    file.seekg(0, std::ios::beg);
    file.read(&t[0], t.size());

    nlohmann::json j = nlohmann::json::parse(t);

    return j;
}
}

#endif