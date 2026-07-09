import requests

def get_advice():
  response = requests.get("https://api.adviceslip.com/advice")
  data  = response.json()
  print(response.status_code)
  # print(data)

  if response.status_code == 200:
    return f"{data['slip']['advice']}"
  else:
    return "Couldn't fetch advice right now"
  
result = get_advice()
print(result)


def get_country_info(code):
  response = requests.get(f"https://countries.dev/alpha/{code}")
  data = response.json()
  # print(data)
  # print(response.text)
  print(response.status_code)

  if response.status_code == 200:
    name = data["name"]
    capital = data["capital"]
    population = data["population"]

    return f"{name}'s capital is {capital} with a population of {population}"
  else:
    print("Couldn't fetch advice right now")

result = get_country_info("in")
print(result)