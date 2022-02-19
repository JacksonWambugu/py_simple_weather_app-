import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api="http://api.weatherapi.com/v1/current.json?key=cf3d521f16d7409380630504221902&q=" +  city + "&aqi=no"
    json_data = requests.get(api).json()
    condition = json_data['current']['condition']['text']
    temp = int(json_data['current']['temp_c'])
    preasure = json_data['current']['pressure_mb']
    humidity=json_data['current']['humidity']
    final_info = condition + "\n" + str(temp) + "°C"
    final_data="\n Pressure :: " + str(preasure) + "\n Humidity :: " + str(humidity)

    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfield=tk.Entry(canvas,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas,font=t)
label1.pack()

label2=tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()