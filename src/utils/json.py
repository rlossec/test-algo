import json
from typing import Any, Dict


def load_json(path: str) -> Dict[str, str]:
    with open(path, "r") as f:
        return json.load(f)


def save_json(data: Dict[str, str], path: str) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
