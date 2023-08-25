"""
web_server:
  host: 127.0.0.1
  port: 80
    
db_server:
  host: 127.0.0.1
  port: 3306
"""

import yaml

with open('section11/config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)
    
with open('section11/config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    