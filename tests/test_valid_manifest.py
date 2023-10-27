# FIXME perhaps we should not have this one, because of Pydantic v1/v2 issues

import json
import sys
from pathlib import Path

import requests
from devtools import debug

import PROJECTNAME


def test_valid_manifest(tmp_path):
    """
    NOTE: to avoid adding a fractal-server dependency, we simply download the
    relevant file.
    """
    # Download Pydantic model for ManifestV1
    url = (
        "https://raw.githubusercontent.com/fractal-analytics-platform/"
        "fractal-server/main/fractal_server/app/schemas/manifest.py"
    )
    r = requests.get(url)
    with (tmp_path / "fractal_manifest.py").open("wb") as fp:
        fp.write(r.content)

    sys.path.append(tmp_path.as_posix())
    from fractal_manifest import ManifestV1

    module_dir = Path(PROJECTNAME.__file__).parent
    manifest_file = module_dir / "__FRACTAL_MANIFEST__.json"
    debug(manifest_file)
    with manifest_file.open("r") as fin:
        manifest_dict = json.load(fin)
    manifest = ManifestV1(**manifest_dict)
    debug(manifest)
