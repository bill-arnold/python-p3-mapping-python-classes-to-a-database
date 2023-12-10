from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        # SQL statement to create the 'songs' table
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        # Execute the SQL statement
        CURSOR.execute(sql)

    def save(self):
        # SQL statement to insert a new record into the 'songs' table
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        # Execute the SQL statement with bound parameters
        CURSOR.execute(sql, (self.name, self.album))
        
        # Get the ID of the last inserted row and assign it to the instance's id attribute
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        # Create a new Song instance and save it to the database
        song = Song(name, album)
        song.save()
        return song

# Example usage:
# Create the 'songs' table
Song.create_table()

# Create and save a new song
hello = Song.create("Hello", "25")

# Retrieve the saved song's attributes
print(hello.id)    # Should print the assigned ID
print(hello.name)  # Should print "Hello"
print(hello.album)  # Should print "25"
