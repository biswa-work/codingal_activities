# Activity 3: Weather Prediction

weather = (1, 0, 0, 0, 1, 1, 0)

rainy = weather.count(1)
sunny = weather.count(0)

print("Weather records:", weather)
print("Rainy days:", rainy)
print("Sunny days:", sunny)

if rainy > sunny:
    print("Prediction: Rainy weather!")
elif sunny > rainy:
    print("Prediction: Sunny weather!")
else:
    print("Prediction: Balanced weather!")
