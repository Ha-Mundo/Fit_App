def km_to_steps(distance):
    steps_in_one_km = 1312.34
    total_steps = steps_in_one_km * distance
    return total_steps
 
def ask_distance():
    distance_to_office = float(input("Distance from Home to Office in Km: "))
    evening_walk_distance = float(input("How many km is your evening walk?: "))
    return distance_to_office, evening_walk_distance
 

def find_total_distance_walked(distance_to_office, evening_walk_distance):
    office_commute = distance_to_office * 2
    total_distance  = office_commute + evening_walk_distance
    return total_distance
 

def main():
    office_distance, evening_walk_distance = ask_distance()
    total_distance = find_total_distance_walked(office_distance, evening_walk_distance)
    total_steps = km_to_steps(total_distance)
 
    return total_steps
 
total_steps_walked_in_a_day = main()
 
print(f"Total steps = {total_steps_walked_in_a_day} ")