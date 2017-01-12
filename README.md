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
    $ MUSICDB_ROLE=<role> alembic revision --autogenerate -m "<message>"
    ```

1. View the SQL this migration will run
    ```
    $ MUSICDB_ROLE=<role> alembic upgrade head --sql > sql.txt
    ```

1. Actually run the migration
    ```
    $ MUSICDB_ROLE=<role> alembic upgrade head
    ```

## Initial setup

See Google Drive document.

## Queries

* Get all tracks whose album has a particular tag

    ```python
    session.query(Track).filter(Track.album.has(Album.tags.any(name='tango'))).all()
    ```

