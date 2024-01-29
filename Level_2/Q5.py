# You are developing a program that analyzes weather data. Write
# a Python function that takes a list of temperature readings for a
# specific location and determines the average temperature, highest
# temperature, and lowest temperature.
# Input: temperature_readings = [25, 28, 21, 24, 27]
# Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21

def analyze_temperature(temperature_readings):
    average_temperature = sum(temperature_readings) / len(temperature_readings)
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)
    return {
        "Average Temperature": average_temperature,
        "Highest Temperature": highest_temperature,
        "Lowest Temperature": lowest_temperature
    }

temperature_readings = [25, 28, 21, 24, 27]

result = analyze_temperature(temperature_readings)
print("Output:")
for key, value in result.items():
    print(f"{key}: {value}")
