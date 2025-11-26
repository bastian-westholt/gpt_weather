import requests
import json
from src import gpt
import shutil


def responsive_title(text):
    width = shutil.get_terminal_size().columns

    # Bei kleinem Terminal: kürzer
    if len(text) + 10 > width:
        print(f"# {text} #".center(width))
    else:
        # Normal: mit Bindestrichen
        print(f" {text} ".center(width, "-"))


def get_weather_text(weather_code):
    with open('data/weather_code.json', 'r') as Reader:
        content = json.loads(Reader.read())
        return content[weather_code]


def main():
    # FETCHING AND REARRANGING WEATHER-DATA FROM OPEN-METEO API
    res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,weather_code,precipitation_probability,precipitation&current=temperature_2m,weather_code')
    weather_data = res.json()
    weather_code = str(weather_data['current']['weather_code'])
    weather_text = get_weather_text(weather_code)
    weather_data['current']['weather_code'] = weather_text

    # USER-INPUTTED QUESTION
    responsive_title("WELCOME TO WEATHER-GURU")
    print('')
    question = input('Was möchtest du wissen zum Wetter in deiner Region: ')
    meta_prompt = f"""
        Du bist ein Meteorologe und Wetterjournalist und sollst
        zum Wetter in Köln folgende Frage beantworte {question}.
        
        Hier findest du die Wetter-Daten zu Köln:
        {weather_data}
        
        Bitte hab eine professionelle Ansprache und antworte mit
        max. 100 Worten.
        """

    # CHATGPT'S RESPONSE
    gpt_res = gpt.get_gpt_res(meta_prompt)
    print()
    print(gpt_res)
    print()

if __name__ == "__main__":
    main()