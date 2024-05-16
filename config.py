import os
import sys

def add_project_to_path() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, 'src/validators'))
    sys.path.insert(0, project_dir) 