from src.repositories.highscore_repository import HighscoreRepository
from src.database.database_connection import get_database_connection

class HighscoreService():
    def __init__(self):
        self.highscore_repository = HighscoreRepository(
            get_database_connection())

    def get_highscores(self):
        highscores = self.highscore_repository.fetch_highscores()
        return [{'id': row[0], 'score': row[1]} for row in highscores]

    def delete_lowest(self):
        current_highscores = self.highscore_repository.fetch_highscores()

        if len(current_highscores) > 5:
            current_highscores.sort(key=lambda x: x[1])
            for i in range(len(current_highscores) - 5):
                self.highscore_repository.delete_highscore(
                    current_highscores[i][0])

    def add_highscore(self, score):
        self.highscore_repository.insert_highscore(score)
