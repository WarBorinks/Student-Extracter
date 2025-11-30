# ifndef SE_READ
# define SE_READ

# include <fstream>
# include <nlohmann/json.hpp>
# include <stdexcept>
# include <string>

namespace se {
using nlohmann::json;
using std::ifstream;
using std::ios;
using std::runtime_error;
using std::string;

json read(const string& path) {
    ifstream file(path);

    if (!file.is_open()) {
        throw runtime_error("文件损坏！");
    }
    
    string t;
    file.seekg(0, ios::end);
    t.resize(file.tellg());
    file.seekg(0, ios::beg);
    file.read(&t[0], t.size());

    json j = json::parse(t);

    return j;
}
}

# endif