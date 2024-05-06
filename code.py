import time
import board
import adafruit_hcsr04

# Define the maximum and minimum distance values
max_distance = 56.168  # Maximum distance in centimeters
min_distance = 1.87    # Minimum distance in centimeters

# Initialize the ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP9, echo_pin=board.GP8)

def map_value(value, from_low, from_high, to_low, to_high):
    """
    Map the given value from one range to another range.
    """
    return int((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low)

while True:
    try:
        distance = sonar.distance
        # Map the distance value to a percentage
        percentage = 100 - map_value(distance, min_distance, max_distance, 0, 100)
        # Ensure percentage is not negative
        if percentage < 0:
            percentage = 0
        print("Distance:", distance, "cm")
        print("Percentage:", percentage, "%")
    except RuntimeError:
        print("Retrying!")
    time.sleep(1)

