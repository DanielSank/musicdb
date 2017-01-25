import musicdb.client as client
from musicdb.models import Album, Track, Tag


def upload(session):
    tango, _ = client.get_or_create(
            session,
            Tag,
            {'name': "tango"}
    )

    album, _ = client.get_or_create(
            session,
            Album,
            {'name': "Putumayo Presents: Tango Around the World",
             'year': 2007},
            {'tags': [tango]}
    )

    tracks_info = [
            {'name': 'Felino', 'number': 6, 'album': album}
    ]

    tracks = []
    for track_info in tracks_info:
        track = client.get_or_create(
                session,
                Track,
                track_info
        )

