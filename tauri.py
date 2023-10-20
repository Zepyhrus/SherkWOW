import time,  requests,  yaml
from datetime import datetime
from urllib.parse import urlencode
from tqdm import tqdm

with open('cfg.s.yml', 'r') as f:
  cfg = yaml.safe_load(f)
  ae = cfg['APIEndpoint'] # 
  ak = cfg['APIKey']
  sk = cfg['SecretKey']


realm = 'Mistblade'
url = f"{ae}?apikey={ak}"
# url = f'{ae}?apikey={ak}'



def get_guild_list():
  req = {
    'secret': sk,
    'url'    : 'guild-info',
    'params' : {
      'r': realm,
      'gn': 'DADDY SKY GUIDE',
    }
  }

  rep = requests.post(url=url, json=req, verify=True)
  print(rep)

  with open('guild.yml', 'w') as f:
    yaml.safe_dump(rep.json(), f)

def get_raid_maps():
  req = {
    'secret': sk,
    'url'    : 'raid-maps',
    'params' : {
      'r': realm,
    }
  }

  rep = requests.post(url=url, json=req, verify=True)
  print(rep)

  with open('raid_maps.yml', 'w') as f: yaml.safe_dump(rep.json()['response'], f)


def get_raid_rank_encounter():
  req = {
    'secret': sk,
    'url'    : 'raid-rank-encounter',
    'params' : {
      'r': realm,
      'encounter': 1623,
      'difficulty': 5,  # 3 for normal
      'from': 0,
      'limit': 0,
    }
  }

  rep = requests.post(url=url, json=req, verify=True)
  print(rep, rep.text)

  with open('raid_rank_encounter.yml', 'w') as f: 
    yaml.safe_dump(rep.json()['response'], f)


def get_log_id(id):
  req = {
    'secret': sk,
    'url'    : 'raid-log',
    'params' : {
      'r': realm,
      'id': id
    }
  }

  rep = requests.post(url=url, json=req, verify=True)

  if rep.status_code < 300:
    return rep.json()['response']


def get_raid_guild(gname='DADDY SKY GUIDE'):
  req = {
    'secret': sk,
    'url'    : 'raid-guild',
    'params' : {
      'r': realm,
      'gn': gname,
      'from': 0,
      'limit': 0,
    }
  }

  rep = requests.post(url=url, json=req, verify=True)
  print(rep)

  with open('raid-guild.yml', 'w') as f:
    yaml.safe_dump(rep.json()['response'], f)


if __name__ == '__main__':
  # # 5: 10H, 6: 25H
  # # 5.4 SOO encounters: 
  # enc_ids = [1602, 1598, 1624, 1604, 1622, 1600, 1606, 1603, 1595, 1594, 1599, 1601, 1593, 1623]

  # with open('raid-guild.yml', 'r') as f:
  #   rg_logs = yaml.safe_load(f)['logs']


  # valid_logs = [_ for _ in rg_logs if _['difficulty'] in [5, 6] and _['encounter_id'] in enc_ids]

  # print(len(valid_logs))

  # logs = []
  # for valid_log in tqdm(valid_logs):
  #   log = get_log_id(valid_log['log_id'])
  #   logs.append(log)

  # with open('logs.yml', 'a') as f:
  #   yaml.safe_dump(logs, f)

  
  with open('_log.yml', 'r') as f:
    log = yaml.safe_load(f)
  
  kt = datetime.fromtimestamp(log["killtime"])
  print(f'---- {log["encounter_data"]["encounter_name"]} {kt} ----')

  for meb in log['members']:
    _n = meb['name']
    _dps = meb['dmg_done'] / log['fight_time']
    _cls = meb['class']
    _spc = meb['spec']
    _ill = meb['ilvl']

    print(f'{_n}: {_dps}, {_cls}, {_spc} - {_ill}')