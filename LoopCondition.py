time_of_day = list(range(24))
hours = 0

while True:
    for hour in time_of_day:
        print(f"It is {hour} hundred hours.")
        if hour == 23:
            hours += 1
            print(f"It has been {hours} hours!")
        if hours == 5:
            print(f"It has been five iterations.")
            break
#Task 2
# Modify the infinite loop to terminate naturally
time_of_day = list(range(24))
hours = 0

while hours < 5:
    for hour in time_of_day:
        print(f"It is {hour} hundred hours.")
        if hour == 23:
            hours += 1
            print(f"It has been {hours} hours!")


