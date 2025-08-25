from scheduler.availability import find_available_technicians, find_available_equipments
from scheduler.assign import assign_resources_to_sample


def assign_samples_recursively(samples, technicians, equipments, schedule):
    """Assign samples one by one by updating the resources."""

    if not samples:
        return schedule  # No more samples to assign

    # Sort samples by number of available technicians
    samples = sorted(samples, key=lambda s: len(find_available_technicians(s, technicians)))
    sample = samples[0]

    available_technicians = find_available_technicians(sample, technicians)
    available_equipments = find_available_equipments(sample, equipments)

    if not available_technicians or not available_equipments:
        print(f"⚠️ Impossible to assign {sample['id']}, skipping")
        return assign_samples_recursively(samples[1:], technicians, equipments, schedule)

    # Choose technician : specialist > generalist
    chosen_technician = next((t for t in available_technicians if t["speciality"] == sample["type"]), available_technicians[0])
    # Choose equipment (here the first available, but you can optimize)
    chosen_equipment = available_equipments[0]

    # Assign the sample
    assignation = assign_resources_to_sample(sample, chosen_technician, chosen_equipment)
    if assignation:
        schedule.append(assignation)

        # Update the availability of the resources
        chosen_technician["start_time"] = assignation["end_time"]
        chosen_technician["remaining_time"] -= sample["analysis_time"]
        chosen_equipment["start_time"] = assignation["end_time"]

        print(f"✅ Sample {sample['id']} assigned to Tech {chosen_technician['id']} + Equip {chosen_equipment['id']}")

    # Recursive call with the remaining samples
    return assign_samples_recursively(samples[1:], technicians, equipments, schedule)
