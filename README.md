# IoT-Based Cruise Control System

[![Java](https://img.shields.io/badge/Java-17-orange)](https://www.oracle.com/java/)
[![Arduino](https://img.shields.io/badge/Arduino-IDE-orange)](https://www.arduino.cc/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Project Overview

This project demonstrates an **IoT-based cruise control system** that automatically maintains vehicle speed and responds to obstacles in real-time.  
It integrates **Arduino, sensors, and Python monitoring**, simulating real-world automotive cruise control.

**Key highlights:**
- Automatic speed control using **PWM motor control**  
- Obstacle detection using **HC-SR04 ultrasonic sensor**  
- Speed adjustment via **buttons**  
- Real-time **LCD display**  
- Python interface for monitoring speed and distance  

---

## 🛠 Features

- **Cruise Control:** Set target speed with buttons or predefined levels.  
- **Automatic Speed Adjustment:** Adjusts throttle to maintain stable speed.  
- **Obstacle Detection:** Detects nearby obstacles and reduces speed.  
- **LCD Display:** Shows current speed and obstacle distance.  
- **Python Monitoring:** Real-time speed and distance logging.


---

## 🔧 Hardware Requirements

- Arduino Uno  
- DC Motor + Motor Driver Module  
- HC-SR04 Ultrasonic Sensor  
- 16x2 LCD Module  
- Push Buttons  
- Jumper Wires & Breadboard  
- Power Supply  

---

## 💻 Software Requirements

- Arduino IDE  
- Python 3.x  
- Python Libraries:  
  - `gpiozero` (for GPIO & PWM)  
  - `RPi.GPIO` (optional, Raspberry Pi)  
  - `lcd` (optional, for physical LCD)  

---

## ⚡ How It Works

1. Arduino reads **sensor inputs** (speed & obstacle distance).  
2. Motor speed is adjusted using **PWM** to maintain cruise speed.  
3. **Buttons** allow manual increase/decrease of speed.  
4. Python program monitors speed and distance in **real-time**.  
5. Ultrasonic sensor automatically **reduces speed** if an obstacle is detected.  
6. LCD shows current **speed and distance**.

---

## 🚀 Setup Instructions

1. Connect hardware following the **circuit diagram**.  
2. Upload `CruiseControlSystem.ino` to Arduino.  
3. Run `cruise_control.py` on your computer or Raspberry Pi.  
4. Press buttons to set cruise speed and watch obstacle response.  
5. Monitor speed and distance via **Python console or LCD**.  

---

## 📈 Applications

- Automotive **cruise control systems**  
- IoT **vehicle automation**  
- Embedded systems prototyping  
- Smart robotics projects  

---

## 👨‍💻 Author

**Sharukesh U** – MCA Student | Vellore Institute of Technology  
Email: sharukesh790@gmail.com | Phone: +91 82485 61892  

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
---

## 📁 Project Structure
