import PROJECTNAME
import json
from pathlib import Path


PACKAGE = "PROJECTNAME"
PACKAGE_DIR = Path(PROJECTNAME.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
