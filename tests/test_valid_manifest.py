# FIXME perhaps we should not have this one, because of Pydantic v1/v2 issues

import sys

import requests
from devtools import debug

from . import MANIFEST


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

    manifest = ManifestV1(**MANIFEST)
    debug(manifest)
