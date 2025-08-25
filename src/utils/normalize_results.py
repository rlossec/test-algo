from config import PRIORITY_ORDER

# Invert the PRIORITY_ORDER dictionary
PRIORITY_ORDER_INVERTED = {v: k for k, v in PRIORITY_ORDER.items()}

def normalize_schedule(schedule):
    """Normalize the schedule to be a list of dictionaries with the following keys:
    - sampleId
    - technicianId
    - equipmentId
    - startTime
    - endTime
    - priority
    """

    normalized_schedule = []
    for assignation in schedule:
        normalized_schedule.append({
            "sampleId": assignation["sample_id"],
            "technicianId": assignation["technician_id"],
            "equipmentId": assignation["equipment_id"],
            "startTime": assignation["start_time"].strftime("%H:%M"),
            "endTime": assignation["end_time"].strftime("%H:%M"),
            "priority": PRIORITY_ORDER_INVERTED[assignation["priority"]],
        })

    # Sort by startTime
    normalized_schedule.sort(key=lambda x: x["startTime"])

    return normalized_schedule


