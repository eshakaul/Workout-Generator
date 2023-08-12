import random
import json
WORKOUT_DATA = 'data/workouts.json'


def create_workout(num_exercises):
    with open(WORKOUT_DATA, 'r') as file:
        exercises = json.load(file)['exercises']
        
    # Randomly sample exercises
    sampled_exercises = random.sample(exercises, num_exercises)
    
    workout_message = "############################################\n"
    workout_message += "##########  Today's Workout: ##############\n"
    workout_message += "############################################\n"
    for i, exercise in enumerate(sampled_exercises, start=1):
        workout_message += f"Exercise {i}: {random.randint(3, 5)}x{random.choice([10,15,20])}, {exercise['Exercise']}\n"
        workout_message += f"Details: {exercise['Key Details']}\n"
        workout_message += f"Targeted Muscle Group: {exercise['Targeted Muscle Group']}\n"
        workout_message += "\n"
    
    return workout_message

workout = create_workout(10)
print(workout)  