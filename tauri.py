import time,  requests,  yaml, matplotlib.pyplot as plt
plt.rcParams['figure.autolayout'] = True
plt.rcParams['axes.facecolor'] = 'black'

import numpy as np, pandas as pd
from datetime import datetime
from urllib.parse import urlencode
from tqdm import tqdm


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


def get_log_by_id(id):
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


def get_raid_guild(gname='DADDY SKY GUIDE', limit=20):
  assert limit <= 1000, 'No more than 1000 logs allowed!'
  rg_logs = []
  req = {
    'secret': sk,
    'url'    : 'raid-guild',
    'params' : {
      'r': realm,
      'gn': gname,
      'from': 0,
      'limit': 1000,
    }
  }

  rep = requests.post(url=url, json=req, verify=True)
  _logs = rep.json()['response']['logs']
  
  for _log in _logs:
    if _log['difficulty'] not in [5, 6]: continue # 非10人或者25人
    if _log['encounter_id'] not in enc_ids: continue  # 非SOO
    if _log['log_id'] in set([_['log_id'] for _ in rg_logs]): continue  # 重复的LOG 
  
    rg_logs.append(_log)

    if len(rg_logs) >= limit:
      break
  return rg_logs
  
  


if __name__ == '__main__':
  with open('cfg.s.yml', 'r') as f:
    cfg = yaml.safe_load(f)
    ae = cfg['APIEndpoint'] # 
    ak = cfg['APIKey']
    sk = cfg['SecretKey']

  realm = 'Mistblade'
  url = f"{ae}?apikey={ak}"

  # 5: 10H, 6: 25H
  # 5.4 SOO encounters: 
  enc_ids = [1602, 1598, 1624, 1604, 1622, 1600, 1606, 1603, 1595, 1594, 1599, 1601, 1593, 1623]
  valid_logs = get_raid_guild(limit=20)

  # print(len(valid_logs))

  logs = []
  for valid_log in tqdm(valid_logs):
    log = get_log_by_id(valid_log['log_id'])
    logs.append(log)
  
  for i, log in tqdm(enumerate(logs)):
    if not log: continue

    kt = datetime.fromtimestamp(log["killtime"]).strftime("%Y/%m/%d %H-%M-%S")
    _ft = log["fight_time"]/60000
    ft = f'{int(_ft)} min {(_ft-int(_ft))*60:.2f} s'
    
    _classes =   cfg['Class']
    _specs = cfg['Specs']
    df = pd.DataFrame({
      'name': [_['name'] for _ in log['members']],
      'dps': [_['dmg_done']/log['fight_time'] for _ in log['members']],
      'class': [_classes[_['class']] for _ in log['members']],
      'spec': [ _specs[_classes[_['class']]][_['spec']] for _ in log['members']],
      'ilvl': [_['ilvl'] for _ in log['members']],
    })
    df.sort_values('dps', ignore_index=True, inplace=True)
    df['color'] = [cfg['Colors'][_] for _ in df['class']]
    # print(df.head())

    # draw
    fig, ax = plt.subplots(figsize=(12,8))
    y_pos = np.arange(len(df['dps']))
    hbars = ax.barh(y_pos, df['dps'], color=df['color'])
    ax.set_yticks(y_pos, labels=df['name'])
    ax.set_yticklabels(labels=df['name'], rotation=45)
    labels = [str(z)+'/'+x+'-'+f'{y:.2f}' for x, y, z in zip(df['spec'], df['dps'], df['ilvl'])]
    ax.bar_label(hbars, labels=labels, color='white', padding=8)
    ax.set_xlim(0, 1.2*df['dps'].max())
    ax.set_title(f'- {log["encounter_data"]["encounter_name"]}, {ft}, {kt} -')

    if len(df) > 10:
      subfolder = 'H25'
    else:
      subfolder = 'H10'
    
    # if 'Tyman' in list(df['name']):
    #   prex = 'Tyman_'
    # elif 'Deinss' in list(df['name']):
    #   prex = 'Deinss_'
    # else:
    prex = ''

    plt.savefig(f'pics\\{i}_{subfolder}.png')
    plt.close()


