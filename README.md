# E-Ink Desk Display

 This project is a Python-based e-ink display manager designed for a Waveshare 2.13-inch V4 e-ink display. It dynamically updates real-time weather information, system usage (CPU, memory, and temperature), and displays a variety of random faces. The project is built for a Raspberry Pi setup.
 
<img src="https://github.com/Toast7529/E-Ink-Desk-Display/blob/main/Assets/doc/E-Ink.jpg" alt="Generated Display" width="200"/>
<img src="https://github.com/Toast7529/E-Ink-Desk-Display/blob/main/Assets/doc/Generated.png" alt="Generated Display" width="200"/>
 

# Features:
- **Real-Time Weather Updates:** Fetches live weather data from the [OpenWeatherMap API](https://openweathermap.org/), showing the current temperature in the selected city. Icons are displayed alongside the temperature.
- **System Monitoring:** The display shows key system stats such as CPU usage, CPU temperature, & memory usage
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
## Autostart:
To automatically start the display on boot, a `systemd` service file can be used:
1) Create a service file:
```bash
sudo nano /etc/systemd/system/e-ink-display.service
```
2) Copy & paste into `e-ink-display.service`:
```bash
[Unit]
Description=E-Ink Desk Display
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/E-Ink-Desk-Display/E-Ink-Desk-Display/main.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```
3) Reload `systemd` and enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable e-ink-display
sudo systemctl start e-ink-display
```
