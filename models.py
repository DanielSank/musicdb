from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


TRACK_NAME_LEN = 64
ALBUM_NAME_LEN = 64
GENRE_NAME_LEN = 64
URL_LEN = 255


Base = declarative_base()


class Track(Base):

    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(TRACK_NAME_LEN), nullable=False)

    # many -> one
    album_id = Column(Integer, ForeignKey('albums.id'), nullable=True)
    album = relationship('Album', back_populates='tracks')

    # one -> many
    urls = relationship('URL', back_populates='track')


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    value = Column(String(URL_LEN), nullable=False, unique=True)

    # many -> one
    track_id = Column(Integer, ForeignKey('tracks.id'), nullable=False)
    track = relationship('Track', back_populates='urls')


album_genre = Table('album_genre', Base.metadata,
        Column('album_id', Integer, ForeignKey('albums.id')),
        Column('genre_id', Integer, ForeignKey('genres.id')))


class Album(Base):

    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(ALBUM_NAME_LEN), nullable=False)
    year = Column(Integer, nullable=True)

    # one -> many
    tracks = relationship('Track', back_populates='album')

    # many -> many
    genres = relationship(
            'Genre',
            secondary=album_genre,
            back_populates='albums')


class Genre(Base):

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(GENRE_NAME_LEN), nullable=False, unique=True)

    # many -> many
    albums = relationship(
            'Album',
            secondary=album_genre,
            back_populates='genres')

