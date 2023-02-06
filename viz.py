import requests






if __name__ == '__main__':
  url = 'https://tauriprogress.github.io/raid/Siege%20of%20Orgrimmar/Immerseus' # ?class=&difficulty=5&faction=&realm=&role=tank&tab=0'

  # url = 'https://www.w3schools.com/python/demopage.php'
  # myobj = {'somekey': 'somevalue'}

  headers = {
    "Host": "www.propertyshark.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
  }

  obj = {
    'difficulty': 5
  }

  x = requests.post(url, headers=headers , json = obj)

  print(x.text)



