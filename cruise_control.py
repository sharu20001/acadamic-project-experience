import serial
import time

# Connect to Arduino
arduino = serial.Serial('COM3', 9600)   # Change COM port if needed
time.sleep(2)

speed = 60
cruise_limit = 100
distance = 0

print("Cruise Control System Started")

while True:
    
    try:
        data = arduino.readline().decode().strip()

        # Expected format from Arduino: speed,distance
        values = data.split(",")

        if len(values) == 2:
            speed = int(values[0])
            distance = int(values[1])

            print("Current Speed:", speed)
            print("Obstacle Distance:", distance)

            # Cruise speed control
            if speed < cruise_limit:
                print("Increasing throttle")

            elif speed > cruise_limit:
                print("Reducing throttle")

            else:
                print("Maintaining speed")

            # Obstacle detection logic
            if distance <= 5:
                print("STOP! Obstacle very close")

            elif distance <= 15:
                print("Reducing speed - obstacle detected")

            elif distance <= 35:
                print("Obstacle ahead - slowing down")

            print("-----------------------")

    except:
        print("Waiting for sensor data...")
