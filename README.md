# musicdb

This is an SQL schema and indexing scripts for music collections.

## Configure your virtualenv

1. `$ pip install -r requirements.txt`

1. Add the directory containing this project to your virtualenv's PYTHONPATH.
If you're using virtualenvwrapper and the project is in `~/src/musidb`, then do
    ```
    $ add2virtualenv ~/src
    ```

## Migration

1. Generate alembic migration from models
    ```
    $ alembic revision --autogenerate -m "<message>"
    ```

1. View the SQL this migration will run
    ```
    $ alembic upgrade head --sql > sql.txt
    ```

1. Actually run the migration
    ```
    $ alembic upgrade head
    ```

## Initial setup

You don't need to do this. This is notes for myself on how to set up at the very beginning.

1. Install requirements and initialize alembic

    ```
    $ pip install -r requirements.txt
    $ alembic init alembic
    ```

1. In `alembic.ini`, change the database url to 'bogus'.

1. In `alembic/env.py`, add the following blocks:
    ```python
    # Get the full database url
    import config as myconfig
    config.set_main_option(
        'sqlalchemy.url',
         myconfig.config.get('DB_URL'))

    # Add models' MetaData object for 'autogenerate' support.
    # We assume that the project root is in the system path
    import models as models
    target_metadata = models.Base.metadata
    ```

