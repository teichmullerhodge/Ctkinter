import requests
import OpenWeather
import customtkinter

from PIL import Image
from CTkColorPicker import *


def get_curr_weather(q):


    api_key = OpenWeather.api_key #Your file with your api Key
   

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={q}&aqi=no'

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()
    
        location_data = data['location']


        name = location_data['name']
        region = location_data['region']
        country = location_data['country']
        latitude = location_data['lat']
        longitude = location_data['lon']
        curr_time = location_data['localtime']

        

        current_data = data['current']


        temperature_c = current_data['temp_c']
        day_night = current_data['is_day'] #0 if is night

        wind_speed = current_data['wind_kph'] #in kph
        humidity = current_data['humidity']
        therm_sensation = current_data['feelslike_c']

        current_condition_data = data['current']['condition']
    

        current_condition = current_condition_data['text']
        image_condition_path = current_condition_data['icon']


        city_label.configure(text=f"{name.upper()}")
        temperature_label.configure(text=f"{temperature_c:.0f}°C")

        current_time_label.configure(text=f'{curr_time.split(" ")[1]}')
        condition_label.configure(text=f'{current_condition}')

        hours, minutes = map(int, curr_time.split(" ")[1].split(":"))
        total_minutes = hours * 60 + minutes

        if total_minutes < 360 or total_minutes > 1080:
            customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
        else:
            customtkinter.set_appearance_mode("light")


        if 'rain' in current_condition:
            condition_button.configure(image=RAIN_IMAGE)
        if 'clear' in current_condition:
            condition_button.configure(image=CLEAR_IMAGE)
        if 'snow' in current_condition:
            condition_button.configure(image=SNOW_IMAGE)

        temp_value = int(temperature_c)

        if temp_value >= 24:
            therm_button.configure(image=TERM_IMAGE)
        if temp_value > 13 and temp_value < 24:
            therm_button.configure(image=TERM_MIDDLE_IMAGE)
        if temp_value < 13:
            therm_button.configure(image=TERM_COLD_IMAGE)


        print(f"In {name} feels like {therm_sensation}, the current temperature is {temperature_c}")
        print(f"Wind speed is {wind_speed}, the current condition is {current_condition}, at {curr_time}")

    


    else:
        print(f"A solicitação falhou com código de status: {response.status_code}")

#WINDOW CONFIGURATION

app = customtkinter.CTk()
app.title("WeaTkinter")
app.geometry('600x400')

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark


#IMAGES CONFIGURATION


SUN_IMAGE = customtkinter.CTkImage(Image.open('sun.png'), size=(26,26))
MOON_IMAGE = customtkinter.CTkImage(Image.open('moon.png'), size=(20,20))
CLEAR_IMAGE = customtkinter.CTkImage(Image.open('clear.png'), size=(26,26))
RAIN_IMAGE = customtkinter.CTkImage(Image.open('rain.png'), size=(26,26))
TERM_IMAGE = customtkinter.CTkImage(Image.open('term.png'), size=(26,26))
TERM_MIDDLE_IMAGE = customtkinter.CTkImage(Image.open('term_middle.png'), size=(26,26))
TERM_COLD_IMAGE = customtkinter.CTkImage(Image.open('term_cold.png'), size=(26,26))
THEME_IMAGE = customtkinter.CTkImage(Image.open('theme.jpg'), size=(26,26))
SNOW_IMAGE = customtkinter.CTkImage(Image.open('snow.png'), size=(26,26))



q_label = customtkinter.CTkLabel(app, text="CITY", font=('Ubuntu Mono', 20))
q_label.grid(row=0, column=0)

q_entry = customtkinter.CTkEntry(app)
q_entry.grid(row=1, column=0)

get_weather_button = customtkinter.CTkButton(app, text="Get Weather Data", fg_color='#1520A6', command=lambda: get_curr_weather(q_entry.get()))
get_weather_button.grid(row=2, column=0, padx=20, pady=10)

city_label = customtkinter.CTkLabel(app, text="Londrina", font=('Ubuntu Mono', 25))
city_label.grid(row=0, column=1, sticky='w', padx=20)


temperature_label = customtkinter.CTkLabel(app, text="°C", font=('Ubuntu Mono', 25))
temperature_label.grid(row=1, column=1, sticky='e', padx=50)

therm_button = customtkinter.CTkButton(app, text="", image=TERM_IMAGE, width=2, fg_color='transparent', hover=False)
therm_button.grid(row=1, column=1, sticky='w', padx=10)

condition_button = customtkinter.CTkButton(app, text='', image=CLEAR_IMAGE, width=2, fg_color='transparent', hover=False)
condition_button.grid(row=1, column=1, sticky='e', padx=10)


condition_label = customtkinter.CTkLabel(app, text="",  font=('Ubuntu Mono', 15))
condition_label.grid(row=0, column=2, padx=20)

current_time_label = customtkinter.CTkLabel(app, text="", font=('Ubunto Mono', 25))
current_time_label.grid(row=1, column=2, padx=20)

theme_button = customtkinter.CTkButton(app, text="", width=2, image=THEME_IMAGE, fg_color='transparent')
theme_button.grid(row=2,column=2, padx=20)


get_curr_weather("Londrina") #londrina as default


app.mainloop()












