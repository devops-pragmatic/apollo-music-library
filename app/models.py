from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sample(db.Model):
    """
    Example model for demonstration. Replace or extend for your assignment.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


# --- Sample Music Library Models ---
class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    albums = db.relationship("Album", backref="artist", lazy=True)


class Album(db.Model):
    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    songs = db.relationship("Song", backref="album", lazy=True)


class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)
    length_seconds = db.Column(db.Integer)


# ------------------------------------------------------------------------
