# Vishnu Ajay
# 10/10/2023
# Python Code for Raspberry Pi with text-to-speech and COWSAY output
# Rev A

import serial
import os
import pyttsx3  # Using text-to-speech library for announcements

# Initialize serial communication with the connected Arduino device
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    try:
        # Read sensor value from Arduino
        sensor_value = int(ser.readline().decode().strip())

        # Map sensor value to servo angle
        servo_angle = int((sensor_value / 1023) * 180)

        # Create an announcement with the servo angle
        announcement = f"Servo angle is {servo_angle} degrees."
        engine.say(announcement)   # Speak the announcement
        engine.runAndWait()        # Wait until speech is done

        # Announce the servo angle using COWSAY
        os.system(f"cowsay Servo Angle: {servo_angle}")

    except KeyboardInterrupt:
        ser.close()  # Close serial connection on interrupt
        break
