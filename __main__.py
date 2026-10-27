import sys
import os
import importlib

# Configure console encoding for Unicode support (e.g. ₹ symbol)
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Ensure project and parent directory are in sys.path
_project_root = os.path.dirname(os.path.abspath(__file__))
_parent_dir = os.path.dirname(_project_root)
_pkg_name = os.path.basename(_project_root)

for d in [_parent_dir, _project_root]:
    if d not in sys.path:
        sys.path.insert(0, d)

if __name__ == "__main__":
    utils_main = importlib.import_module(f"{_pkg_name}.utils.main")
    utils_main.main()
