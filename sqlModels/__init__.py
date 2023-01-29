import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
import os
import random

yaml_config = yaml.load(open(os.environ['DATABASECONFIG']), Loader=yaml.FullLoader)

leader = yaml_config['leader']
replicas = yaml_config['replicas']

leader_engine = create_engine(
        f"postgresql://{leader['username']}:{leader['password']}@{leader['host']}:{leader['port']}/{leader['database']}",
        logging_name='leader',
    )


read_engine=leader_engine
read_engines = []
read_engines.append(leader_engine)
for replica_name in replicas:
    replica = replicas[replica_name]
    read_engines.append(create_engine(
        f"postgresql://{replica['username']}:{replica['password']}@{replica['host']}:{replica['port']}/{replica['database']}",
        logging_name=replica_name,
    ))

# You want to set write to true either when you are writing to the database or when you want to read from the leader
def select_engine(user_id=-1, write=False):
    if write:
        return leader_engine
    elif user_id == -1:
        return random.choice(read_engines)
    else:
        # PYTHONHASHSEED is set to 1 in virtual environment activate file
        return read_engines[hash(str(user_id)) % len(read_engines)]
        
