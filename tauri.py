import requests
import yaml


with open('cfg.yml', 'r') as f:
  cfg = yaml.safe_load(f)
  ae = cfg['APIEndpoint'] # 
  ak = cfg['APIKey']
  sk = cfg['SecretKey']


response = requests.get(f"http://chapi.tauri.hu/apiIndex.php?apikey={ak}")
print(response)


