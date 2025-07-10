# 🌦️ Prince's Beautiful Weather App
# Uses OpenWeatherMap API to fetch live weather
# Built with Tkinter + Requests
import tkinter as tk
import requests

# 🔑 API Key (replace with yours)
API_KEY = "d475a2f672cd89541a5c625847609086"  # Replace with your actual API key

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="❗ Please enter a city name.")
        return
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") != 200:
            result_label.config(text="🚫 City not found.")
            return

        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result = (
            f"📍 {name}, {country}\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"📈 Pressure: {pressure} hPa\n"
            f"🌥️ Condition: {description.title()}\n"
            f"💨 Wind: {wind} m/s"
        )
        result_label.config(text=result)

    except Exception as e:
        result_label.config(text="❌ Error fetching weather.")

# 🎨 GUI Setup
window = tk.Tk()
window.title("🌤️ Prince's Weather App")
window.geometry("420x500")
window.config(bg="#1e1e1e")

# 🧾 Heading with emoji
heading = tk.Label(window, text="🌍 Enter City Name", font=("Segoe UI", 18), bg="#1e1e1e", fg="white")
heading.pack(pady=(20, 10))

# 🔲 Simulate glow using Frame
entry_frame = tk.Frame(window, bg="#00cec9", padx=2, pady=2)
entry_frame.pack(pady=10)

city_entry = tk.Entry(entry_frame, font=("Segoe UI", 16), bg="#2d2d2d", fg="white", bd=0, justify="center", insertbackground="white")
city_entry.pack(ipadx=10, ipady=10)

# 🟩 Button
get_btn = tk.Button(window, text="🔍 Get Weather", font=("Segoe UI", 14), bg="#00b894", fg="white", bd=0, padx=10, pady=10, command=get_weather, activebackground="#55efc4")
get_btn.pack(pady=20)

# 📋 Result Display
result_label = tk.Label(window, text="", font=("Segoe UI", 14), bg="#1e1e1e", fg="#dfe6e9", justify="center")
result_label.pack(padx=20, pady=10)

window.mainloop()
# Note: Make sure to install the requests library if you haven't already