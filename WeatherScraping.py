import requests
def get_city(city_name):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f9e1aac3badf5babfd4604ef9a3f6611"
    data = city_name
    r = requests.get(url.format(data)).json()
    try:
        cw = {"city":data,"temperature":r["main"]["temp"],"description":r["weather"][0]["description"],"icon":r["weather"][0]["icon"]} 
        context = {"cityzone":cw}
        print(context)
    except Exception:
                   print("Invalid city")
         
city = input("Enter the city:")
get_city(city)
