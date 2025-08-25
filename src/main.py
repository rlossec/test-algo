from utils.json import load_json, save_json

DATA_PATH = "../data"
PRIORITY_ORDER = {
  "STAT": 0,
  "URGENT": 1,
  "ROUTINE": 2
}


def parse_data(data: dict) -> tuple[list, list, list]:
  samples = data["samples"]
  technicians = data["technicians"]
  equipment = data["equipment"]
  return samples, technicians, equipment


def sort_samples(samples: list) -> list:
  return sorted(samples, key=lambda x: PRIORITY_ORDER[x["priority"]])


def main():

  data = load_json(f"{DATA_PATH}/input/tests/test_priorities.json")
  # Parse data
  samples, technicians, equipment = parse_data(data)

  # Sort by priority (STAT, URGENT, ROUTINE)

  samples = sort_samples(samples)
  print("sorted samples", samples)

  # Assign resources

  # Planify

  # Calculate metrics


  save_json(data, f"{DATA_PATH}/output/tests/results.json")


if __name__ == "__main__":
    main()
