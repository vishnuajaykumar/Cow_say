# Servo Motion Control with Light Intensity

**Author**: Vishnu Ajay  
**Date**: 10/10/2023  
**Revision**: A  

This project demonstrates the use of a **photoresistor** to control the angle of a **servo motor** based on light intensity. The setup consists of two main parts: an Arduino controlling the servo and a Raspberry Pi providing audio and visual feedback. The project integrates **text-to-speech** functionality and even uses **COWSAY** for fun announcements!

---

## 🛠 Hardware Components

- **Arduino** with a servo motor and photoresistor
- **Raspberry Pi** for text-to-speech and additional feedback
- **Photoresistor** connected to the Arduino to measure light intensity
- **Servo motor** connected to Arduino to adjust its angle based on the sensor input
- **Speaker** connected to Raspberry Pi for audio feedback

---

## 💻 Software Components

### Arduino Code (C++):
- Reads the light intensity from the photoresistor using the **analogRead()** function.
- Maps the sensor value (0-1023) to a servo angle (0-180 degrees).
- Controls the servo motor to adjust its position based on the light levels.

### Raspberry Pi Code (Python):
- Reads the sensor value transmitted via serial communication from the Arduino.
- Converts the sensor value to a servo angle and announces it using **pyttsx3** (text-to-speech engine).
- Uses **COWSAY** to display the servo angle in a humorous way through a terminal cow speech bubble.

---

## 🚀 Setup Instructions

### Arduino:
1. Connect the **photoresistor** to **A0** and the **servo motor** to **pin 9**.
2. Upload the Arduino code (`Servo_Motion.ino`) to your Arduino board.

### Raspberry Pi:
1. Ensure **`pyttsx3`** and **`COWSAY`** are installed:
   ```bash
   pip install pyttsx3
   sudo apt-get install cowsay
