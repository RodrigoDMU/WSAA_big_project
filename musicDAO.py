# -----------------------------------------------------------------------------------------------------
# File: Music DAO provides methods to perform CRUD (Create, Read, Update, Delete) operations.
# -----------------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
# -----------------------------------------------------------------------------------------------------

# Import libraries.
import mysql.connector
import dbconfig as cfg  # Import database configuration (host, user, password, database).


class MusicDAO:
    
    def __init__(self):
        # Initialize database connection parameters from config file.
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self):
        # Establish a new connection to the MySQL database. 
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        # Create a cursor object to execute SQL queries.
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        # Close cursor and connection to free resources.
        self.cursor.close()
        self.connection.close()

# CRUD operations.        
        
    def getAll(self):
        # Retrieve all records from the 'music' table.
        cursor = self.getcursor()
        sql = """SELECT id, artist, title, minutes, year, category 
                 FROM music"""
        cursor.execute(sql)
        results = cursor.fetchall()  # Fetch all results.

        returnArray = []
        # Convert each tuple result to a dictionary.
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll() # Close DB connection.
        return returnArray # Return list of music dictionaries.

    def findByID(self, id):
        # Retrieve a single music record by its ID.
        cursor = self.getcursor()
        sql = """SELECT id, artist, title, minutes, year, category 
                 FROM music 
                 WHERE id = %s"""
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()# Fetch one record.

        self.closeAll()
        if result:
            return self.convertToDictionary(result) # Convert tuple to dict if found.
        else:
            return None # Return None if not found.

    def create(self, music):
        # Insert a new music record into the database.
        cursor = self.getcursor()
        sql = """INSERT INTO music (artist, title, minutes, year, category) 
                 VALUES (%s, %s, %s, %s, %s)"""
        values = (
            music.get("artist"),
            music.get("title"),
            music.get("minutes"),
            music.get("year"),
            music.get("category"),
        )
        cursor.execute(sql, values)
        self.connection.commit() # Commit transaction.

        newid = cursor.lastrowid # Get the auto-generated ID.
        music["id"] = newid  # Add ID to the music dictionary.

        self.closeAll()
        return music # Return the music dictionary including the new ID.

    def update(self, id, music):
        # Update an existing music record by ID.
        cursor = self.getcursor()
        sql = """UPDATE music
                 SET artist=%s, title=%s, minutes=%s, year=%s, category=%s 
                 WHERE id=%s"""
        values = (
            music.get("artist"),
            music.get("title"),
            music.get("minutes"),
            music.get("year"),
            music.get("category"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()  # Commit transaction.
        self.closeAll()

    def delete(self, id):
        # Delete a music record by ID.
        cursor = self.getcursor()
        sql = """DELETE FROM music 
                 WHERE id = %s"""
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit() # Commit transaction.
        self.closeAll()
        
    def convertToDictionary(self, resultLine):
        # Convert a tuple from SQL query result into a dictionary.
        keys = ['id', 'artist', 'title', 'minutes', "year", "category"]
        music = {}
        for i, attrib in enumerate(resultLine):
            music[keys[i]] = attrib
        return music

# Instantiate a single MusicDAO object to be used by the Flask app.
musicDAO = MusicDAO()

# END.