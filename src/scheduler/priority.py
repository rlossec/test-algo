
def sort_samples(samples: list[dict]):
    print(samples)
    return sorted(samples, key=lambda x: x["priority"])


if __name__ == "__main__":
    # Tests priority order
    from pprint import pprint
    from utils.io_json import load_json
    from parsers.parser import parse_data
    DATA_PATH = "../data"
    data = load_json(f"{DATA_PATH}/input/tests/test_priorities.json")
    samples, technicians, equipments = parse_data(data)
    sorted_samples = sort_samples(samples)
    pprint(sorted_samples)