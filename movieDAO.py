import mysql.connector
import dbconfig as cfg


class MovieDAO:
    
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
        sql="""SELECT id, title, minutes, year, category 
               FROM movie"""
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="""SELECT id, title, minutes, year, category 
               FROM movie 
               WHERE id = %s"""
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, movie):
        cursor = self.getcursor()
        sql="""INSERT INTO movie (id, title, minutes, year, category) 
               VALUES (%s, %s, %s, %s, %s)"""
        values = (
            movie.get("title"),
            movie.get("minute"),
            movie.get("year"),
            movie.get("category"),
        )
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        movie["id"] = newid
        self.closeAll()
        return movie


    def update(self, id, movie):
        cursor = self.getcursor()
        sql = """UPDATE movie
                SET title=%s, minutes=%s, year=%s, category=%s 
                WHERE id=%s"""
        print(f"Update movie {movie}")
        values = (
            movie.get("title"),
            movie.get("minutes"), 
            movie.get("year"), 
            movie.get("categoru"), 
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql = """DELETE FROM movie 
                WHERE id = %s"""
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        

    def convertToDictionary(self, resultLine):
        keys=['id','title','minutes', "year", "category"]
        movie = {}
        currentkey = 0
        for attrib in resultLine:
            movie[keys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return movie

        
movieDAO = MovieDAO()