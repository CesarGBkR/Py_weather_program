from tkinter import *
from tkinter import ttk
from environ import API_KEY
import requests

def request():
    city = nombre.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q=" + city

    weather_data = requests.get(base_url).json()
    main = "Main: " + weather_data['weather'][0]['main']
    description = "Description: " + weather_data['weather'][0]['description']
    temp = "Temperature: " + str(weather_data['main']['temp'])
    temp_min = "Minimum expected temperature: " + str(weather_data['main']['temp_min'])
    temp_max = "Maximum expected temperature: " + str(weather_data['main']['temp_max'])
    pressure = "Pressure: " + str(weather_data['main']['pressure'])
    humidity = "Humidity: " + str(weather_data['main']['humidity'])

    ttk.Label(frm, text=main).grid(column=1, row=4)
    ttk.Label(frm, text=description).grid(column=1, row=5)
    ttk.Label(frm, text=temp).grid(column=1, row=6)
    ttk.Label(frm, text=temp_min).grid(column=1, row=7)
    ttk.Label(frm, text=temp_max).grid(column=1, row=8)
    ttk.Label(frm, text=pressure).grid(column=1, row=9)
    ttk.Label(frm, text=humidity).grid(column=1, row=10)


root = Tk()
root.geometry("800x600")
frm = ttk.Frame(root, padding=200)
frm.grid()

# Style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Elements

# Entry
ttk.Label(frm, text='Search your country:').grid(column=1, row=0)
nombre=StringVar()
nomb=ttk.Entry(frm, textvariable=nombre).grid(column=1, row=1)
# Buttons
ttk.Button(frm, text="Search", command=request).grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)

root.title("API Call") # Title
root.mainloop()
