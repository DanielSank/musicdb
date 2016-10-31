TRACK_NAME_LEN =
ALBUM_NAME_LEN =
COMPOSER_NAME_LEN =


class Track(Base):

    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(TRACK_NAME_LEN), nullable=False)

    album_id = Column(Integer, ForeignKey('albums.id'), nullable=True)
    album = relationship('Album', back_populates='tracks')


class Album(Base):

    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(ALBUM_NAME_LEN), nullable=False)

    # one -> many
    tracks = relationship('Track', back_populates='album')


class Composer(Base):

    __tablename__ = 'composers'

    id = Column(Integer, primary_key=True)
    name = Column(String(COMPOSER_NAME_LEN), nullable=False)


# TODO: Link composers to Tracks


class Group(Base):

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(GROUP_NAME_LEN), nullable=False)


class Genre(Base):

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(GENRE_NAME_LEN), nullable=False)


