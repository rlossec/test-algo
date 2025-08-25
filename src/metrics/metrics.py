

def calculate_metrics(schedule: list, technicians: list, equipment: list) -> dict:
  """Calculate metrics for the schedule."""

  # Calculate total time
  start_time = min(sample["start_time"] for sample in schedule)
  end_time = max(sample["end_time"] for sample in schedule)
  total_time = (end_time - start_time).total_seconds() / 60

  analysis_time = sum(sample["analysis_time"] for sample in schedule)

  # Calculate efficiency
  efficiency = analysis_time / total_time

  # Calculate conflicts
  conflicts = 0

  metrics = {
    "totalTime": total_time,
    "efficiency": round(efficiency * 100, 2), # In percentage
    "conflicts": conflicts,
  }
  return metrics