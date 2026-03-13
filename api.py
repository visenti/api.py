import requests
def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=pt"
    response = requests.get(url)
     # Exibindo o status code e a resposta da API para diagnóstico
    print("Código de status:", response.status_code)
    print("Respota da API:", response.text)
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        county = data["sys"]["county"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Previsão do tempo para {city}, {country}:")
        print(f"Temperatura: {temp}°C")
        print(f"Condição: {weather_desc.capitalize()}")
        print(f"Umidade: {humidity}%")
        print(f"Velocidade do Vento: {wind_speed} m/s")
    else:
        print("Erro ao obter os dados. Verifique o nome da cidade e tente novamente.")
 
if __name__ == "__main__":
    API_KEY = "482b8c48f006dde8f978d8afdedfcf1" # Substitua pela sua chave de Bobão
    cidade = input("Digite o nome da cidade:")
    get_weather(cidade, API_KEY)
