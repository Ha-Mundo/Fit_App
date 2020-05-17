# Calories = Weight (in Kg) x 0,0005 x Steps


def weight_steps():
    number = 0.0005
    weight =  float(input("Enter your weight (in Kg):"))
    total_steps_walked_in_a_day = float(input("Enter your steps per day:"))
    total_calories = (weight * number) * total_steps_walked_in_a_day
    
    return total_calories
    
total_burned_calories = weight_steps()
print(f"Total Calories Burned -----> {total_burned_calories} Kcal.")