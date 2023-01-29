import yaml
yaml_config =yaml.load(open('postgresSingle.yaml'), Loader=yaml.FullLoader)

#db_config
host = yaml_config['host']
username = yaml_config['username']
password = yaml_config['password']
port = yaml_config['port']
database = yaml_config['database']