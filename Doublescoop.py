import random
times = ["Morning","Afternoon","Evening"]
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
moods = ["Happy" , "Sad" , "Energetic" , "Calm"]

for day in days:
    mood = random.choice(moods)
    time = random.choice(times)
    print(f"On {day} {time} you were {mood}.")
