import json
from pathlib import Path

from types import SimpleNamespace

def _load_config():
    global CFG
    with open(Path.cwd() / "config.json", "r") as fp:
        data = json.load(fp)
        CFG = SimpleNamespace(**data)