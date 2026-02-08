#ifndef SE_BASIC_EXTRACTER
#define SE_BASIC_EXTRACTER

#include <cstdlib>
#include <ctime>

#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

#include <nlohmann/json.hpp>

#include "read.hpp"

namespace se {
std::vector<std::string> extract_students(const std::string& path) {
    nlohmann::json students = se::read(std::string("students/") + path);

    if (students.size() < 8) {
        throw std::runtime_error("学生人数不足 8 人！");
    }

    srand(time(nullptr));
    std::set<std::string> selected;
    while (selected.size() < 8) {
        for (const auto& [name, prob] : students.items()) {
            double x = (double)(rand() % 1000) / 1000;
            if (x < prob) {
                selected.insert(name);
            }

            if (selected.size() >= 8) {
                break;
            }
        }
    }

    return std::vector<std::string>(selected.begin(), selected.end());
}
}

#endif