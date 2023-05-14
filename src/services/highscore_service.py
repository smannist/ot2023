from repositories.highscore_repository import HighscoreRepository
from database.database_connection import get_database_connection


class HighscoreService():
    """HighscoreService class handles the logic for fetching, adding, and deleting highscores
    """
    def __init__(self):
        """Creates a single HighscoreService class object

        Args:
             highscore_repository (object): HighscoreRepository class for handling database management
        """
        self.highscore_repository = HighscoreRepository(
            get_database_connection())

    def get_highscores(self):
        """Fetch all highscores and reformat them into a list of dictionaries

        Returns:
            List: A list of dictionaries where each dictionary represents a highscore by a single player
        """
        highscores = self.highscore_repository.fetch_highscores()
        return [{'id': row[0], 'score': row[1]} for row in highscores]

    def delete_lowest(self):
        """Deletes the lowest highscores until only the top 5 remain
        """
        current_highscores = self.highscore_repository.fetch_highscores()

        if len(current_highscores) > 5:
            current_highscores.sort(key=lambda x: x[1])
            for i in range(len(current_highscores) - 5):
                self.highscore_repository.delete_highscore(
                    current_highscores[i][0])

    def add_highscore(self, score):
        """Inserts a highscore into the highscores table

        Args:
            score (int): The highscore to be inserted
        """
        self.highscore_repository.insert_highscore(score)
