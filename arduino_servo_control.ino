// VISHNU AJAY
// 10/10/2023
// Photo Resistor to Servo angle
// REV A

#include <Servo.h> // Servo Library

int photoSensorPin = A0; // Pin connected to the photoresistor
int servoPin = 9;        // Pin connected to the servo
Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(photoSensorPin, INPUT);  // Set up as input for sensor
  myServo.attach(servoPin);        // Attach servo to pin
}

void loop() {
  int sensorValue = analogRead(photoSensorPin);
  Serial.println(sensorValue);     // Print sensor value

  int servoAngle = map(sensorValue, 0, 1023, 0, 180); // Map sensor value to servo angle
  myServo.write(servoAngle);       // Set servo position

  delay(1000); // 1 second delay
}
