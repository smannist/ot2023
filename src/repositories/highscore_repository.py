
class HighscoreRepository:
    """HighscoreRepository class handles interaction with the highscores table in the database

    Attributes:
        connection (object): SQLite database connection object
    """
    def __init__(self, connection):
        """Class constructor which creates a single HighscoreRepository object
        
        Args:
            connection (object): SQLite database connection object
        """
        self._connection = connection
        self.cur = self._connection.cursor()

    def fetch_highscores(self):
        """Fetch all highscores from the highscores table ordered in decending order

        Returns:
            list: A list of tuples where each tuple represents a row in the highscores table
        """
        return self.cur.execute("SELECT * FROM highscores ORDER BY score DESC").fetchall()

    def insert_highscore(self, score):
        """Inserts a highscore into the highscores table

        Args:
            score (int): The highscore to be inserted
        """
        self.cur.execute("""INSERT INTO highscores (score)
                            VALUES (?)""", (score,))
        self._connection.commit()

    def delete_highscore(self, id):
        """Deletes a highscore from the highscores table

        Args:
            id (int): The id of the highscore to be deleted
        """
        self.cur.execute("DELETE FROM highscores WHERE id = ?", (id,))
        self._connection.commit()
