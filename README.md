# IoT-Based Cruise Control System

[![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D?logo=arduino&logoColor=white)](https://www.arduino.cc/)
[![C++](https://img.shields.io/badge/C%2B%2B-17-00599C?logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Project Overview

This project demonstrates an **IoT-based cruise control system** that automatically maintains vehicle speed and responds to obstacles in real time. It uses **Arduino Uno, sensors, and embedded programming** to simulate a real-world automotive cruise control system.

**Key highlights:**
- Automatic speed control using **PWM motor control**
- Obstacle detection using the **HC-SR04 ultrasonic sensor**
- Speed adjustment using **push buttons**
- Real-time **LCD display** for speed and obstacle distance

---

## 🛠 Features

- **Cruise Control:** Set and maintain a target speed using push buttons.
- **Automatic Speed Adjustment:** Uses PWM to maintain a stable motor speed.
- **Obstacle Detection:** Detects nearby obstacles and automatically reduces speed.
- **LCD Display:** Displays the current speed and obstacle distance in real time.
- **Embedded Control:** Implements cruise control logic directly on the Arduino.

---

## 🔧 Hardware Requirements

- Arduino Uno
- DC Motor
- Motor Driver Module
- HC-SR04 Ultrasonic Sensor
- 16×2 LCD Module
- Push Buttons
- Jumper Wires
- Breadboard
- Power Supply

---

## 💻 Software Requirements

- Arduino IDE
- Arduino AVR Boards Package

---

## ⚡ How It Works

1. The Arduino continuously reads the ultrasonic sensor to measure obstacle distance.
2. The desired speed is set using push buttons.
3. PWM signals control the DC motor to maintain the selected speed.
4. If an obstacle is detected within a predefined distance, the system automatically reduces the motor speed.
5. The LCD displays the current speed and obstacle distance in real time.

---

## 🚀 Setup Instructions

1. Assemble the hardware according to the circuit diagram.
2. Open `CruiseControlSystem.ino` in the Arduino IDE.
3. Select the correct **Board** (Arduino Uno) and **COM Port**.
4. Upload the sketch to the Arduino.
5. Power on the circuit and use the push buttons to control the cruise speed.
6. Observe the motor speed and LCD display while testing obstacle detection.

---
