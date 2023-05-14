import unittest
from repositories.highscore_repository import HighscoreRepository
from services.highscore_service import HighscoreService
from database.database_connection import get_database_connection
from database.initialize_database import initialize_database, drop_tables

class TestHighscoreService(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.highscore_repository = HighscoreRepository(self.connection)
        self.highscore_service = HighscoreService()

        initialize_database()

        self.highscore_repository.insert_highscore(100)

    def test_highscores_are_fetched_correctly(self):
        highscores = self.highscore_service.get_highscores()

        score = [score["score"] for score in highscores]

        self.assertEqual(score[0], 100)
        self.assertEqual(len(highscores), 1)

        drop_tables(self.connection)
