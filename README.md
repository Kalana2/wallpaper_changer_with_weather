# 🌦️ Dynamic Weather-Based Wallpaper Changer


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


This Python-based project is a smart desktop wallpaper engine that automatically changes your wallpaper based on real-time weather conditions for a given location — making your workspace visually dynamic and mood-matching!

## 💡 Features

- 🌤 **Weather Detection:** Fetches real-time weather data from OpenWeatherMap for any city.
- 🖼 **Image Retrieval:** Searches and downloads weather-themed images from Unsplash using the current weather description.
- 🖼 **Dynamic Wallpaper:** Updates your Linux desktop wallpaper (GNOME) to match the live weather.
- 🔄 **Concurrent Execution:** Multi-process architecture ensures smooth operation between weather updates, image downloading, and wallpaper setting.

## 🧰 Tech Stack

- Python 3
- `requests` for HTTP requests
- OpenWeatherMap API for weather data
- Unsplash API for fetching high-quality images
- Multiprocessing for parallel task handling

---

## 🏗️ Project Structure

```
.
🔹 main.py                # Main script to start the wallpaper engine
🔹 engine.py              # Handles setting the downloaded image as wallpaper
🔹 image_downloader.py    # Downloads weather-based images from Unsplash
🔹 weather_check.py       # Fetches real-time weather descriptions from OpenWeatherMap
🔹 /images                # Directory to store downloaded images
```

---

## ⚙️ Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/dynamic-weather-wallpaper.git
cd dynamic-weather-wallpaper
```

2. Install dependencies:

```bash
pip install requests
```

3. Add your API keys in `main.py`:

```python
api_key = "your_openweathermap_api_key"
access_key = "your_unsplash_access_key"
city = "Your_City"
```

4. Run the program:

```bash
python main.py
```

⚡ The program will continuously fetch the weather and update your desktop wallpaper every few seconds!

---

## 🚨 Notes

- Designed for **GNOME desktops** (Linux) — you can extend `engine.py` for other environments.
- Make sure the `images` directory exists.
- You need valid API keys from [OpenWeatherMap](https://openweathermap.org/) and [Unsplash Developers](https://unsplash.com/developers).

---

## 🤝 Contributions

Pull requests are welcome! If you have ideas for extending to Windows or MacOS, feel free to contribute.

---
<!--
## 📜 License

[MIT](LICENSE) — free for personal and commercial use.
-->
