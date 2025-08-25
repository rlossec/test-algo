from datetime import timedelta


def assign_resources_to_sample(sample: dict, technicians: list, equipments: list) -> dict:
    """ Find resources to assign to sample """
    technician_found = False
    equipment_found = False
    assignation = {}
    # Search technicians
    available_technicians = [t for t in technicians if t["available"]]
    print("Available technicians : ", available_technicians)
    for technician in available_technicians:
        # Check if technician has the same speciality as the sample
        if technician["speciality"] != sample["type"]:
            print("##### Technician has the wrong speciality #####")
            continue # Skip and continue with the next one
        # Check if technician has enough remaining time to analyze the sample
        if technician["remaining_time"] < sample["analysis_time"]:
            print("##### Technician has not enough remaining time #####")
            continue # Skip and continue with the next one
        print("##### Technician found #####")
        technician_found = True
        # Search for equipment
        available_equipments = [e for e in equipments if e["available"]]
        print("Available equipments : ", available_equipments)
        for available_equipment in available_equipments:
            if available_equipment["type"] != sample["type"]:
                print("##### Equipment has the wrong type #####")
                continue # Skip and continue with the next one
            print("##### Equipment found #####")
            # Check when equipment can be available
            ## If there is no start time, it means the equipment is available immediately
            if available_equipment.get("start_time") is None:
                print("##### Equipment is available immediately #####")
                # Assignation successful
                equipment_found = True
                start_time = max(technician["start_time"], sample["arrival_time"])
                assignation["sample_id"] = sample["id"]
                assignation["equipment_id"] = available_equipment["id"]
                assignation["technician_id"] = technician["id"]
                assignation["start_time"] = start_time
                assignation["end_time"] = start_time + timedelta(minutes=sample["analysis_time"])
                assignation["priority"] = sample["priority"]
                print("Assignation successful : \n", assignation)
                # Update resources availability
                technician["start_time"] = assignation["end_time"]
                technician["remaining_time"] -= sample["analysis_time"]
                available_equipment["start_time"] = assignation["end_time"]
                break
            ## If there is a start time
            else:
                print("##### Equipment is available after the sample arrival time #####")
                start_time = max(available_equipment["start_time"], sample["arrival_time"], technician["start_time"])
                # Assignation successful
                equipment_found = True
                assignation["sample_id"] = sample["id"]
                assignation["equipment_id"] = available_equipment["id"]
                assignation["technician_id"] = technician["id"]
                assignation["start_time"] = start_time
                assignation["end_time"] = start_time + timedelta(minutes=sample["analysis_time"])
                assignation["priority"] = sample["priority"]
                print("Assignation successful : \n", assignation)
                # Update resources availability
                technician["start_time"] = assignation["end_time"]
                technician["remaining_time"] -= sample["analysis_time"]
                available_equipment["start_time"] = assignation["end_time"]
                break
    
    ## If no technician is available, skip the sample
    if not technician_found or not equipment_found:
        print("No assignation found for sample", sample["id"], "because no technician or equipment was found")
        return None, technicians, equipments
    else:
        # Update active technicians and equipments
        technicians = [t for t in technicians if t["id"] != technician["id"]]
        technicians.append(technician)
        equipments = [e for e in equipments if e["id"] != available_equipment["id"]]
        equipments.append(available_equipment)
        return assignation, technicians, equipments



if __name__ == "__main__":
    from utils.io_json import load_json
    from parsers.parser import parse_data
    from scheduler.priority import sort_samples
    from pprint import pprint

    print("#"*100)
    print("Example 1")

    # Example 1 
    data = load_json("../data/input/tests/example_1.json")
    samples, technicians, equipments = parse_data(data)
    sorted_samples = sort_samples(samples)

    assignation, technicians, equipments = assign_resources_to_sample(sorted_samples[0], technicians, equipments)


    # Example 2
    print("#"*100)
    print("Example 2")

    data = load_json("../data/input/tests/example_2.json")
    samples, technicians, equipments = parse_data(data)
    sorted_samples = sort_samples(samples)

    assignation, technicians, equipments = assign_resources_to_sample(sorted_samples[0], technicians, equipments)

    print("--------------------------------")

    assignation, technicians, equipments = assign_resources_to_sample(sorted_samples[1], technicians, equipments)

    
    print("Technicians : ")
    pprint(technicians)
    print("Equipments : ")
    pprint(equipments)


    # Example 3
    print("#"*100)
    print("Example 3")

    data = load_json("../data/input/tests/example_3.json")
    samples, technicians, equipments = parse_data(data)
    sorted_samples = sort_samples(samples)

    assignation, technicians, equipments = assign_resources_to_sample(sorted_samples[0], technicians, equipments)
    print("--------------------------------")
    assignation, technicians, equipments = assign_resources_to_sample(sorted_samples[1], technicians, equipments)
    print("Second sample assignation : ", assignation)
    print("--------------------------------")

