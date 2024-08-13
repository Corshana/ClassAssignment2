# Attempt to convert the input to a float
# Handle the case where the input is not a number
# If no exception was raised, print the convert temp 
# This block will always happen

def fahrenheit_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

