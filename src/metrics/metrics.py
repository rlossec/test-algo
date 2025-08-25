

def calculate_metrics(schedule: list, technicians: list, equipment: list) -> dict:
  metrics = {
    "totalTime": 0,
    "efficiency": 0.0,
    "conflicts": 0,
  }
  return metrics