from datetime import datetime, timedelta

from scheduler.assign import assign_resources_to_sample
from parsers.parser import parse_data
from utils.io_json import load_json, save_json
from scheduler.priority import sort_samples

DATA_PATH = "../data"


def main():
    # imports
    from scheduler.assign import planify_assignation_over_time
    from metrics.metrics import calculate_metrics

    data = load_json(f"{DATA_PATH}/input/tests/test_priorities.json")
    # Parse data
    samples, technicians, equipment = parse_data(data)
    # Sort by priority (STAT, URGENT, ROUTINE)
    samples = sort_samples(samples)

    schedule = []

    # Iterate over samples
    for sample in samples:
        print("Start assignation for sample", sample["id"])
        # Assign resources
        assignation = assign_resources_to_sample(sample, technicians, equipment)
        # Planify assignation over time
        planified_assignation = planify_assignation_over_time(assignation, technicians, equipment)
        # Update technician and equipment availability
        technicians[assignation["technicianId"]]["available"] = planified_assignation["endTime"]
        equipment[assignation["equipmentId"]]["available"] = False
        # Add to schedule
        schedule.append(planified_assignation)
    print("End all assignations")
    print("Schedule:", schedule)
    # Calculate metrics
    print("Calculating metrics...")
    metrics = calculate_metrics(schedule, technicians, equipment)
    # Format and save results
    results = {
        "schedule": schedule,
        "metrics": metrics
    }
    save_json(results, f"{DATA_PATH}/output/tests/results.json")


if __name__ == "__main__":
    main()
