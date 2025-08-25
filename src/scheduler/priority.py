from config import SORTED_CATEGORIES, PRIORITY_ORDER
from datetime import datetime

def categorize_samples(samples: dict, categories: list[str] = SORTED_CATEGORIES):
    """ Categorize samples by priority """
    return {
        category: [s for s in samples if s["priority"] == PRIORITY_ORDER[category]] for category in categories
    }


if __name__ == "__main__":
    # Tests priority order
    from pprint import pprint
    from utils.io_json import load_json
    from parsers.parser import parse_data

    DATA_PATH = "../data"
    data = load_json(f"{DATA_PATH}/input/tests/test_priorities.json")
    samples, technicians, equipments = parse_data(data)
    categorized_samples = categorize_samples(samples)
    pprint(categorized_samples)