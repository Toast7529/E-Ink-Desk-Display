# E-Ink Desk Display
 This project is a Python-based e-ink display manager designed for a Waveshare 2.13-inch V4 e-ink display. It dynamically updates real-time weather information, system usage (CPU, memory, and temperature), and displays a variety of random faces. The project is built for a Raspberry Pi setup.

# Features:
- **Real-Time Weather Updates:** Fetches live weather data from the [OpenWeatherMap API](https://openweathermap.org/), showing the current temperature in the selected city. Icons are displayed alongside the temperature.
- **System Monitoring:** The display shows key system stats such as:
-  CPU usage and temperature
-  Memory usage
-  System time
- **Periodic Refresh:** The e-ink display refreshes every 12 hours.
# Hardware:
- Display: [Waveshare 2.13-inch V4 e-ink display](https://amzn.eu/d/hemTzxH)
- Host: Raspberry Pi (tested on Pi 5)
# Installation:
1) Clone the repository:
```bash
git clone https://github.com/Toast7529/E-Ink-Desk-Display
```
2) Install required Python packages:
```bash
pip install -r requirements.txt
```
3) Set up your `config.toml`:
- Obtain an API key from [OpenWeatherMap](https://openweathermap.org/)
- Edit `config.toml` file with your API key and desired city.
- Edit `globalTick` in `config.toml` for desired update interval, the default is 3 minutes.
4) Run the script:
```bash
python3 main.py
```
