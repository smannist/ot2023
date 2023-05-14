
class HighscoreRepository:
    def __init__(self, connection):
        self._connection = connection
        self.cur = self._connection.cursor()

    def fetch_highscores(self):
        return self.cur.execute("SELECT * FROM highscores ORDER BY score DESC").fetchall()

    def insert_highscore(self, score):
        self.cur.execute("""INSERT INTO highscores (score)
                            VALUES (?)""", (score,))
        self._connection.commit()

    def delete_highscore(self, id):
        self.cur.execute("DELETE FROM highscores WHERE id = ?", (id,))
        self._connection.commit()
