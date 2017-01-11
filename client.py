from __future__ import print_function


import os


import mutagen
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm.exc import NoResultFound
import yaml


import musicdb.models as models


# UTILITY

def get_url(role=None):
    if role is None:
        role = os.environ['MUSICDB_ROLE']
    home = os.path.expanduser('~')
    config_file_name = os.path.join(home, ".musicdb_config.yml")
    with open(config_file_name, 'r') as stream:
        parameters = yaml.load(stream)[role]
    url = r'mysql+mysqldb://{}:{}@{}'.format(
            parameters['USERNAME'],
            parameters['PASSWORD'],
            parameters['HOST'])
    return url


def make_session(role):
    url = get_url(role)
    engine = sa.create_engine(url, echo=False)
    return orm.sessionmaker(bind=engine)()


def make_yaml_from_file(filepath):
    f = mutagen.File(filepath)
    tags = dict(f.tags)
    d = {}
    d['album'] = tags['album'][0]
    d['composers'] = tags['composer'][0].split('/')
    d['year'] = int(tags['date'][0])
    d['genres'] = tags['genre']
    d['title'] = tags['title']
    d['number'] = int(tags['tracknumber'][0])
    return yaml.safe_dump(d)

