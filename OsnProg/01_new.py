import requests

request_string = "https://belarusbank.by/apiZx/atm"

my_params = {
    "city": "Минск",
    "ATM_currency": "EUR,BYN"
}

response = requests.get(request_string, params = my_params)

if response:
    A = response.json()
    print(A)
else:
    print("О оу")
    print("Код ответа: ", response.status_code)
    print("Причина: ",response.reason) 