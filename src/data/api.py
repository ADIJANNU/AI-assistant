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