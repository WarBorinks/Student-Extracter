#ifndef SE_WRITER
#define SE_WRITER

#include <fstream>
#include <stdexcept>
#include <string>

#include <nlohmann/json.hpp>

namespace se {
void write(std::string path, const nlohmann::json& j, const bool students) {
    if (path[0] == '.') {
        path = "../students" + path.substr(1);
    }

    std::string data;

    if (students) {
        nlohmann::json solved_j;
        for (auto item : j) {
            solved_j[item["name"]] = item["prob"];
        }

        data = solved_j.dump(4);
    } else {
        data = j.dump(4);
    }

    std::ofstream file(path);

    if (!file.is_open()) {
        throw std::runtime_error("目标目录不存在！");
    }

    file << data;
}
}

#endif
