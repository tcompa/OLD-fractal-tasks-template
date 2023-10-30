import MyProject
import json
from pathlib import Path


PACKAGE = "MyProject"
PACKAGE_DIR = Path(MyProject.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
