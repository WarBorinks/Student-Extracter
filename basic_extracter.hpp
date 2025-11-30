# ifndef SE_BASIC_EXTRACTER
# define SE_BASIC_EXTRACTER

# include <cstdlib>
# include <ctime>
# include <iostream>
# include <nlohmann/json.hpp>
# include <set>
# include <stdexcept>
# include <string>

# include "read.hpp"

using nlohmann::json;
using se::read;
using std::cout;
using std::ios;
using std::runtime_error;
using std::set;
using std::string;

namespace se {
int basic_extracter(int argc, char* argv[]) {
    string path("default.students");
    if (argc > 1) {
        path = argv[1];
    }
    json students = read(string("students/") + path);

    if (students.size() < 8) {
        throw runtime_error("学生人数不足 8 人！");
    }

    srand(time(nullptr));
    set<string> selected;
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

    ios::sync_with_stdio(false);
    cout.tie(nullptr);

    for (const string& name : selected) {
        cout << name << "\n";
    }

    return 0;
}
}

# endif