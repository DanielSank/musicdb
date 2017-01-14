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
    config_file_name = os.path.join(home, ".musicdb", "config.yml")
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


def get_or_create(session, model, get_params, create_params=None):
    """Get a or create an instance in the database.
    Args:
        session:
        model: Class of the object to create.
        get_params (dict): parameters needed to uniquely identify an already
            existing entity.
        create_params (dict): Additional parameters needed if the entity does
            not already exist and has to be created

    Returns:
        an ORM object representing the instance.
        (bool): True if the instance was created, False if it already existed.
    """
    if create_params is None:
        create_params = {}
    try:
        instance = session.query(model).filter_by(**get_params).one()
    except NoResultFound:
        instance = None
    if instance:
        created = False
    else:
        all_params = dict(get_params.items() + create_params.items())
        instance = model(**all_params)
        session.add(instance)
        created = True
    return instance, created


def file_to_dict(filepath):
    f = mutagen.File(filepath)
    tags = dict(f.tags)
    d = {}
    d['album'] = tags['album'][0]
    d['composers'] = tags['composer'][0].split('/')
    d['year'] = int(tags['date'][0])
    d['genres'] = tags['genre']
    d['title'] = tags['title']
    d['number'] = int(tags['tracknumber'][0])
    return d


def make_entities(session, data):
    tags = []
    for genre in data['genres']:
        tag, created_tag = get_or_create(
                session,
                models.Tag,
                {'name': genre.lower()})
    album, created_album = get_or_create(
            session,
            models.Album,
            {'name': data['album'], 'year': data['year']})
    track, created_track = get_or_create(
            session,
            models.Track,
            {'name': data['title'], 'number': data['number'], 'album': album})


