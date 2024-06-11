# ORM == Object Relational Mapper
import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()

class Artist:
    @classmethod
    def get_by_id(cls, id):
        """Query the db for artist with id, return an Artist object"""
        sql = f"SELECT ArtistId, Name FROM artists WHERE id={id}"
        cursor.execute(sql).fetchone()
        return Artist(name=row[1], id=row[0])
        
    @classmethod
    def get_all(cls):
        """Query db for all artists, return list of objects"""
        sql = f"""
            SELECT ArtistId, Name
            FROM artists"""
        artists = []
        for row in cursor.execute(sql):
            artist = Artist(name = row[1], id=row[0])
            artists.append(artist)
        return artists
    
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        
    def insert(self):
        """Inserts this artist object into the db"""
        sql=f"""INSERT INTO artists(Name) VALUES("{self.name}")"""
        result = cursor.execute(sql)
        connection.commit()
        self.id = result.lastrowid
        
    def update(self):
        """Updates an existing artist in the db"""
        sql = f"""UPDATE artists SET Name = "{self.name}" WHERE ArtistId = {self.id}"""
        cursor.execute(sql)
        connection.commit()
        
    def save(self):
        """Inserts or updates the artist in the db"""
        if self.id is None:
            self.insert()
        else:
            self.update()
        
    def __repr__(self) -> str:
        return f"<Artist {self.id} {self.name}>"
    
    
    
if __name__ == '__main__':
    # new_artist = Artist(name='test2')
    # new_artist.insert()
    # print(new_artist.id)
    # artist = Artist.get_by_id(1)
    # artist.name = "ac/dc"
    # artist.update()
    # artist = Artist(name='abc')
    # artist.name = "ac/dc"
    # artist.save()
    for a in Artist.get_all():
        print(a)