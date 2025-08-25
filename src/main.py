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


def main():
  #Example 1
  data = load_json(f"{DATA_PATH}/input/tests/example_3.json")
  # Parse data
  samples, technicians, equipment = parse_data(data)
  print("samples", samples)
  print("technicians", technicians)
  print("equipment", equipment)

  # Sort by priority (STAT, URGENT, ROUTINE)

  # Assign resources

  # Planify

  # Calculate metrics


  save_json(data, f"{DATA_PATH}/output/tests/results.json")


if __name__ == "__main__":
    main()
