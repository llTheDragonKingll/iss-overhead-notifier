# 🛰️ ISS Overhead Notifier (Python)

A Python script that checks if the International Space Station (ISS) is overhead at a given location and sends an email notification when it is visible.

---

## 🚀 Features

* 📡 Fetches ISS position using API
* 🌍 Checks whether the ISS is close to a chosen location
* 🌙 Verifies whether it is currently dark enough for visibility
* 📧 Sends an email alert automatically
* ⏱️ Can be scheduled to run at regular intervals using PythonAnywhere

---

## 🛠️ Tech Stack

* Python
* Requests
* SMTP / Email
* PythonAnywhere

---

## 📂 Project Structure

```text
iss-overhead-notifier/
│
├── main.py
└── README.md
```

---

## ⚙️ How to Run

1. Install required libraries:

```bash
pip install requests
```

2. Open `main.py` and update the placeholders:

```python
MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"
MY_LAT = your_lat
MY_LONG = your_long
```

3. Run:

```bash
python main.py
```

---

## 💡 Notes

* Uses public APIs to get ISS location and sunrise/sunset information
* Sends an email only when the ISS is nearby and it is nighttime
* Can be scheduled on PythonAnywhere to run automatically at regular intervals

---

## ⭐ About this project

Built while learning Python and experimenting with APIs, scheduling, and real-world automation.

