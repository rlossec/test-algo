
from datetime import datetime

PRIORITY_ORDER = {"STAT": 0, "URGENT": 1, "ROUTINE": 2}


def parse_data(data: dict) -> tuple[list, list, list]:
  raw_samples = data["samples"]
  raw_technicians = data["technicians"]
  raw_equipment = data["equipment"]

  today = datetime.today()

  # Parse samples
  samples = []
  for raw_sample in raw_samples:
    arrival_time = datetime.combine(today, datetime.strptime(raw_sample["arrivalTime"], "%H:%M").time())
    priority = PRIORITY_ORDER[raw_sample["priority"]]
    sample = {
      "id": raw_sample["id"],
      "type": raw_sample["type"],
      "priority": priority,
      "analysis_time": raw_sample["analysisTime"],
      "arrival_time": arrival_time,
      "patient_id": raw_sample["patientId"]
    }
    samples.append(sample)

  # Parse technicians

  technicians = []
  for raw_technician in raw_technicians:
    start_time = datetime.combine(today, datetime.strptime(raw_technician["startTime"], "%H:%M").time())
    end_time = datetime.combine(today, datetime.strptime(raw_technician["endTime"], "%H:%M").time())
    if start_time >= end_time:
      available = False
    else:
      available = True
      # Calculate remaining time in minutes
      remaining_time = (end_time - start_time).total_seconds() / 60
    technician = {
      "id": raw_technician["id"],
      "speciality": raw_technician["speciality"],
      "start_time": start_time,
      "end_time": end_time,
      "available": available,
      "remaining_time": remaining_time
    }
    technicians.append(technician)

  # Parse equipment
  equipments = []
  for raw_equipment in raw_equipment:
    equipment = {
      "id": raw_equipment["id"],
      "type": raw_equipment["type"],
      "available": raw_equipment["available"]
    }
    equipments.append(equipment)
  return samples, technicians, equipments


# Tests

if __name__ == "__main__":
    # Tests
    from utils.io_json import load_json
    DATA_PATH = "../data"
    data = load_json(f"{DATA_PATH}/input/tests/example_1.json")
    samples, technicians, equipments = parse_data(data)
    print("samples", samples)
    print("technicians", technicians)
    print("equipments", equipments)
