def find_available_technicians(sample, technicians):
    """Retourne les techniciens compatibles avec le sample et dispo."""
    available_technicians = []
    for technician in technicians:
        # Speciality compatible (same type or generalist)
        if technician["speciality"] not in (sample["type"], "GENERAL"):
            continue
        # Enough remaining time
        if technician["remaining_time"] < sample["analysis_time"]:
            continue
        # Check temporal availability
        if technician["start_time"] > sample["arrival_time"]:
            continue
        available_technicians.append(technician)
    return available_technicians


def find_available_equipments(sample, equipments):
    """Retourne les équipements compatibles et dispo."""
    available_equipments = []
    for equipment in equipments:
        if equipment["type"] != sample["type"]:
            continue
        # Equipment available immediately
        if equipment.get("start_time") is None:
            available_equipments.append(equipment)
        # Otherwise, available before or at the arrival of the sample
        elif equipment["start_time"] <= sample["arrival_time"]:
            available_equipments.append(equipment)
    return available_equipments
