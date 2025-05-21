import mysql.connector
import dbconfig as cfg


class MusicDAO:
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
    
        self.connection.close()
        self.cursor.close()

# CRUD operations        
    def getAll(self):
        cursor = self.getcursor()
        sql="""SELECT id,, artist, title, minutes, year, category 
               FROM music"""
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="""SELECT id, artist, title, minutes, year, category 
               FROM music 
               WHERE id = %s"""
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, music):
        cursor = self.getcursor()
        sql="""INSERT INTO music (id,, arstis, title, minutes, year, category) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (
            music.get("artist"),
            music.get("title"),
            music.get("minute"),
            music.get("year"),
            music.get("category"),
        )
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        music["id"] = newid
        self.closeAll()
        return music


    def update(self, id, music):
        cursor = self.getcursor()
        sql = """UPDATE music
                SET artist=%s, title=%s, minutes=%s, year=%s, category=%s 
                WHERE id=%s"""
        print(f"Update music {music}")
        values = (
            music.get("title"),
            music.get("minutes"), 
            music.get("year"), 
            music.get("category"), 
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql = """DELETE FROM music 
                WHERE id = %s"""
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        

    def convertToDictionary(self, resultLine):
        keys=['id', 'artist', 'title','minutes', "year", "category"]
        music = {}
        currentkey = 0
        for attrib in resultLine:
            music[keys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return music

        
musicDAO = MusicDAO()