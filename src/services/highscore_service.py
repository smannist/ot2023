from repositories.highscore_repository import HighscoreRepository
from database.database_connection import get_database_connection

class HighscoreService():
    def __init__(self) -> None:
        self.highscore_repository = HighscoreRepository(get_database_connection())
    
    def get_highscores(self):
        highscores = self.highscore_repository.fetch_highscores()
        return [{'score': row[0]} for row in highscores]
    
    def add_highscore(self, score):
        self.highscore_repository.insert_highscore(score)
