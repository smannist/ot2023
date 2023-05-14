from database.database_connection import get_database_connection

# drop_tables is used for testing
def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS highscores;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INT
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
