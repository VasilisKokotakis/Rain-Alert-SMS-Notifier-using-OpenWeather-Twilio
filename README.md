
```text
██████╗  █████╗ ██╗███╗   ██╗     █████╗ ██╗     ███████╗██████╗ 
██╔══██╗██╔══██╗██║████╗  ██║    ██╔══██╗██║     ██╔════╝██╔══██╗
██████╔╝███████║██║██╔██╗ ██║    ███████║██║     █████╗  ██████╔╝
██╔═══╝ ██╔══██║██║██║╚██╗██║    ██╔══██║██║     ██╔══╝  ██╔══██╗
██║     ██║  ██║██║██║ ╚████║    ██║  ██║███████╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
```

# 🌦 Rain Alert SMS Notifier using OpenWeather & Twilio

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![OpenWeather](https://img.shields.io/badge/API-OpenWeather-orange?logo=openstreetmap)](https://openweathermap.org/forecast5)
[![Twilio](https://img.shields.io/badge/API-Twilio-red?logo=twilio)](https://www.twilio.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project checks the weather forecast using the **OpenWeather API** and sends you an **SMS alert via Twilio** if rain is expected.
Never forget your umbrella again! ☔

---

## 📸 Demo

> Example SMS:

```
☔ Rain is expected today. Don’t forget your umbrella!
```

---

## ⚙️ Features

* ✅ Fetches real-time weather data from [OpenWeather](https://openweathermap.org/forecast5)
* ✅ Predicts upcoming rain (next few forecast hours)
* ✅ Sends SMS notifications via [Twilio](https://www.twilio.com/)
* ✅ Secure setup with environment variables (no hardcoding secrets)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Rain-Alert-SMS-Notifier-using-OpenWeather-Twilio.git
cd Rain-Alert-SMS-Notifier-using-OpenWeather-Twilio
```

### 2. Install dependencies

```bash
pip install requests twilio
```

### 3. Set environment variables

Replace the placeholders with your own keys:

**Linux / macOS**

```bash
export OWM_API_KEY="your_openweather_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_account_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
```

**Windows (Powershell)**

```powershell
setx OWM_API_KEY "your_openweather_api_key"
setx TWILIO_ACCOUNT_SID "your_twilio_account_sid"
setx TWILIO_AUTH_TOKEN "your_twilio_auth_token"
```

### 4. Run the script

```bash
python main.py
```

---

## 🛠 Configuration

Inside `main.py`, set your coordinates:

```python
MY_LAT  = 1.352083   # Example: Singapore latitude
MY_LONG = 103.819839 # Example: Singapore longitude
```

---

## 📡 APIs Used

* 🌍 [OpenWeather Forecast API](https://openweathermap.org/forecast5)
* 📲 [Twilio SMS API](https://www.twilio.com/docs/sms)

---

## 📌 To-Do / Ideas

* [ ] Add email notification support
* [ ] Allow multiple recipients
* [ ] Dockerize the project for easy deployment
* [ ] Add support for daily forecast summary

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

✨ Made with Python, ☁️ OpenWeather, and 📱 Twilio.
