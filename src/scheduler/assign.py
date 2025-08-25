from datetime import timedelta


def assign_resources_to_sample(sample: dict, technicians: list, equipment: list) -> dict:
  assignation = {
    "sampleId": sample["id"],
    "technicianId": "",
    "equipmentId": "",
  }
  return assignation



def planify_assignation_over_time(technician: dict, equipment: dict, sample: dict) -> dict:
  planified_assignation = {
    "sampleId": sample["id"],
    "technicianId": technician["id"],
    "equipmentId": equipment["id"],
    "startTime": "",
    "endTime": ""
  }
  return planified_assignation

