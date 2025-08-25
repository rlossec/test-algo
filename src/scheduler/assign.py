from datetime import timedelta


from datetime import timedelta

def assign_resources_to_sample(sample, chosen_technician, chosen_equipment):
    """
    Assign a technician and an equipment to a sample. r
    Return an assignation with planning.
    """

    if not chosen_technician or not chosen_equipment:
        return None

    # The start time is the max between :
    # - the arrival of the sample
    # - the availability of the technician
    # - the availability of the equipment
    start_time = max(
        sample["arrival_time"],
        chosen_technician["start_time"],
        chosen_equipment.get("start_time", sample["arrival_time"]) 
        # When the equipment was not used, no start time property, 
        # so we use the arrival time to stay neutral
    )

    end_time = start_time + timedelta(minutes=sample["analysis_time"])

    assignation = {
        "sample_id": sample["id"],
        "technician_id": chosen_technician["id"],
        "equipment_id": chosen_equipment["id"],
        "start_time": start_time,
        "end_time": end_time,
        "analysis_time": sample["analysis_time"],
        "priority": sample["priority"],
    }

    return assignation



if __name__ == "__main__":
    pass

