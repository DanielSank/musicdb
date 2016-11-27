from __future__ import print_function

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm.exc import NoResultFound

import models


try:
    import config
except ImportError as e:
    message = e.args[0]
    message = message + ("\nFollow instructions in setup.md to "
                         "create config.py.")
    e.args = (message,)
    raise

engine = sa.create_engine(config.config['DB_URL'], echo=False)
Sessionmaker = orm.sessionmaker(bind=engine)


# UTILITY

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


def get_one(session, model, params):
    return session.query(model).filter_by(**params).one()

