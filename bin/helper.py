def get_resources_path(rel_path:str):
    import os, sys
    
    if rel_path.startswith("."):
        if getattr(sys, "frozen", False):
            bin_dir = os.path.dirname(sys.executable)
        else:
            bin_dir = os.path.dirname(os.path.abspath(__file__))
            
        students_dir = os.path.join(os.path.dirname(bin_dir), "students")
        file_name = rel_path[2:]
        return os.path.join(students_dir, file_name)
    else:
        return rel_path

def extract_students(path:dict):
    from pyd_module import extract_students
    return extract_students(path)

def read(path:str):
    from pyd_module import read
    return read(get_resources_path(path))

def write(path:str, data:dict, is_students:bool=True):
    from pyd_module import write
    return write(get_resources_path(path), data, is_students)
    