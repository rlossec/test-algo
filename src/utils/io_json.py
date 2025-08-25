import json
from typing import Dict, Any


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r") as f:
        return json.load(f)


def save_json(data: Dict[str, Any], path: str) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# Tests
if __name__ == "__main__":
    from pathlib import Path
    # Tests load_json
    DATA_PATH = "../../data"
    data = load_json(f"{DATA_PATH}/input/tests/test_priorities.json")
    print(data)
    data = {
        "samples": "sample_example",
        "technicians": "technician_example",
        "equipments": "equipment_example"
    }

    # Tests save_json
    save_json(data, f"{DATA_PATH}/output/tests/test_priorities.json")
    assert Path(f"{DATA_PATH}/output/tests/test_priorities.json").exists()

