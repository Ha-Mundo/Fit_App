def bio_data():
    
    weight_in_kg = float(input("Enter your weight (in Kg):"))
    height_in_cm = float(input("Enter your height (in Cm):"))
    age_in_years = int(input("Enter your age:"))
   
    return weight_in_kg, height_in_cm, age_in_years


def bmr_calculation():
    weight_in_kg, height_in_cm, age_in_years = bio_data()
    calculation = 88.362 + (13.397 * weight_in_kg) + (4.799 * height_in_cm) - (5.677 * age_in_years)

    return calculation

total_man_bmr = bmr_calculation()
print(f"Total man BMR:\n{total_man_bmr} Kcal/day.")

