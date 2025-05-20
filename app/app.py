from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from .config import get_database_url
from .models import Album, Artist, Song, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Auto-init DB and sample data
with app.app_context():
    db.create_all()
    if Artist.query.count() == 0:
        from .sample_data import populate_sample_data

        populate_sample_data()


@app.route("/")
def index():
    artists = Artist.query.all()
    return render_template("index.html", artists=artists)


@app.route("/artist/<int:artist_id>")
def artist_detail(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    return render_template("artist_detail.html", artist=artist)


@app.route("/album/<int:album_id>")
def album_detail(album_id):
    album = Album.query.get_or_404(album_id)
    return render_template("album_detail.html", album=album)


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            db.session.add(Artist(name=name))
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("add_artist.html")


@app.route("/add_album/<int:artist_id>", methods=["GET", "POST"])
def add_album(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            db.session.add(Album(title=title, artist_id=artist_id))
            db.session.commit()
            return redirect(url_for("artist_detail", artist_id=artist_id))
    return render_template("add_album.html", artist=artist)


@app.route("/add_song/<int:album_id>", methods=["GET", "POST"])
def add_song(album_id):
    album = Album.query.get_or_404(album_id)
    if request.method == "POST":
        title = request.form.get("title")
        length = request.form.get("length_seconds")
        if title:
            db.session.add(Song(title=title, album_id=album_id, length_seconds=int(length or 0)))
            db.session.commit()
            return redirect(url_for("album_detail", album_id=album_id))
    return render_template("add_song.html", album=album)


@app.route("/health")
def health():
    """Health check endpoint for monitoring."""
    return {"status": "ok"}, 200


# TODO: Implement music library endpoints here

if __name__ == "__main__":
    # For local dev only; use Gunicorn in production
    app.run(host="0.0.0.0", port=5000)
