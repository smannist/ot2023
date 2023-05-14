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

    def test_highscore_is_added_successfully(self):
        self.highscore_service.add_highscore(100)

        highscores = self.highscore_service.get_highscores()

        score = [score["score"] for score in highscores]

        self.assertEqual(score[0], 100)
        self.assertEqual(len(highscores), 1)

        drop_tables(self.connection)

    def test_highscores_are_fetched_correctly(self):
        self.highscore_service.add_highscore(100)

        highscores = self.highscore_service.get_highscores()

        score = [score["score"] for score in highscores]

        self.assertEqual(score[0], 100)
        self.assertEqual(len(highscores), 1)

        drop_tables(self.connection)

    def test_lowest_score_is_deleted_if_there_are_more_than_5_entries(self):
        for i in range(1, 7):
            self.highscore_service.add_highscore(i*100)

        highscores = self.highscore_service.get_highscores()

        self.assertEqual(len(highscores), 6)

        self.highscore_service.delete_lowest()

        highscores = self.highscore_service.get_highscores()

        self.assertEqual(len(highscores), 5)

        drop_tables(self.connection)

    def test_lowest_score_is_not_deleted_if_there_are_less_than_5_entries(self):
        for i in range(1, 4):
            self.highscore_service.add_highscore(i*100)

        highscores = self.highscore_service.get_highscores()

        self.assertEqual(len(highscores), 3)

        self.highscore_service.delete_lowest()

        highscores = self.highscore_service.get_highscores()

        self.assertEqual(len(highscores), 3)

        drop_tables(self.connection)
