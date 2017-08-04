from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

    # def __init__(self, game_id, name, description):
    #     self.game_id = game_id
    #     self.name = name
    #     self.description = description


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    game1 = Game(name='Game1', description='the first game')
    db.session.add(game1)
    db.session.commit()




if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 