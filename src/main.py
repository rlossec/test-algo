
from pprint import pprint

from parsers.parser import parse_data
from utils.io_json import load_json, save_json

from config import SORTED_CATEGORIES
from scheduler.priority import categorize_samples
from scheduler.recursive import assign_samples_recursively
from metrics.metrics import calculate_metrics
from utils.normalize_results import normalize_schedule

DATA_PATH = "../data"


def main():
    data = load_json(f"{DATA_PATH}/input/tests/example_1.json")
    samples, technicians, equipments = parse_data(data)

    categorized_samples = categorize_samples(samples, SORTED_CATEGORIES)
    schedule = []

    for category in SORTED_CATEGORIES:
        schedule = assign_samples_recursively(categorized_samples[category], technicians, equipments, schedule)

    print(schedule)

    
    metrics = calculate_metrics(schedule, technicians, equipments)
    results = {
        "schedule": normalize_schedule(schedule),
        "metrics": metrics
    }
    
    pprint(results)
    save_json(results, f"{DATA_PATH}/output/tests/results.json")


if __name__ == "__main__":
    main()
