import requests

from io import BytesIO
from PIL import Image


api_server = "http://static-maps.yandex.ru/1.x/"

lon = 37.530887
lat = 55.703118
delta = 5.0

my_params = {
    "ll": f"{lon},{lat}",
    "spn": f"{delta},{delta}",
    "l": "map"
}

response = requests.get(api_server, params=my_params)

if response:
    f = open("picture.png","wb")
    f.write(response.content)
    f.close
else:
    print("Что-то пошло не так.")
    print("Код ответа:", response.status_code)
    print("Причина:", response.reason)
