import random

moods = ["Happy" , "Sad" , "Energetic" , "Calm"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]

for day in days:
    mood = random.choice(moods)

    print(f"On {day} you were feeling {mood}.")
