from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


TRACK_NAME_LEN = 64
ALBUM_NAME_LEN = 64
TAG_NAME_LEN = 64
URL_LEN = 255


Base = declarative_base()


track_tag = Table('track_tag', Base.metadata,
        Column('track_id', Integer, ForeignKey('tracks.id')),
        Column('tag_id', Integer, ForeignKey('tags.id')))


class IPythonPrettyPrintable(object):
    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else '...')


class Track(Base, IPythonPrettyPrintable):

    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(TRACK_NAME_LEN), nullable=False)

    # many -> one
    album_id = Column(Integer, ForeignKey('albums.id'), nullable=True)
    album = relationship('Album', back_populates='tracks')

    # one -> many
    urls = relationship('URL', back_populates='track')

    # many -> many
    tags = relationship(
            'Tag',
            secondary=track_tag,
            back_populates='tracks')

    def __str__(self):
        return 'Track(name={})'.format(self.name)


class URL(Base, IPythonPrettyPrintable):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    value = Column(String(URL_LEN), nullable=False)

    # many -> one
    track_id = Column(Integer, ForeignKey('tracks.id'), nullable=False)
    track = relationship('Track', back_populates='urls')


album_tag = Table('album_tag', Base.metadata,
        Column('album_id', Integer, ForeignKey('albums.id')),
        Column('tag_id', Integer, ForeignKey('tags.id')))


class Album(Base, IPythonPrettyPrintable):

    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(ALBUM_NAME_LEN), nullable=False)
    year = Column(Integer, nullable=False)

    # one -> many
    tracks = relationship('Track', back_populates='album')

    # many -> many
    tags = relationship(
            'Tag',
            secondary=album_tag,
            back_populates='albums')

    def __str__(self):
        return 'Album(name={})'.format(self.name)

    __table_args__ = (UniqueConstraint('name', 'year', name='name_year_uc'),)


class Tag(Base, IPythonPrettyPrintable):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(TAG_NAME_LEN), nullable=False, unique=True)

    # many -> many
    albums = relationship(
            'Album',
            secondary=album_tag,
            back_populates='tags')

    tracks = relationship(
            'Track',
            secondary=track_tag,
            back_populates='tags')

    def __str__(self):
        return 'Tag(name={})'.format(self.name)

