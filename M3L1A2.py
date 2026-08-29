#weather condition
def print_weather_condition(condition):
    if condition == "sunny":
        print("It's a bright and sunny day!")
    elif condition == "rainy":
        print("Don't forget your umbrella, it's raining!")
    elif condition == "snowy":
        print("It's snowing! Stay warm!")
    else:
        print("Weather condition not recognized.")