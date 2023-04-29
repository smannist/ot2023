from database.database_connection import get_database_connection

class HighscoreRepository:
    def __init__(self, connection):
        self._connection = connection
        self.cur = self._connection.cursor()

    def fetch_highscores(self):
        return self.cur.execute("SELECT * FROM highscores").fetchall()

    def insert_highscore(self, score):
        self.cur.execute("""INSERT INTO highscores (score)
                            VALUES (?)""", (score,))
        self._connection.commit()

