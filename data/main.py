import sqlite3
from datetime import datetime
import pytz 
import json


class DataBase:
    def __init__(self, path : str = "data/data.sqlite", settings_path : str = "data/data.json") -> None:
        self.path = path
        
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name, region, registred);""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS admins  (id INTEGER PRIMARY KEY, name, region, registred);""")
        
        conection.commit()
        conection.close()

        # Creating temorary data
        self.users = self.get_users()
        self.admins = self.get_admins()
    

        self.settings_path = settings_path

        js = open(settings_path, 'r')
        self.data = json.loads(js.read())
        js.close()

    def update(self):
        js = open(self.file, 'w')
        js.write(json.dumps(self.data))
    

    def get_users(self) -> dict:
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        data =  {user[0] : {'name' : user[1], 'region' : user[2], 'registred' : user[3]} for user in cursor.execute("SELECT * FROM users;")}

        conection.commit()
        conection.close()

        return data
    
    def get_admins(self) -> dict:
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        data =  {user[0] : {'name' : user[1], 'region' : user[2], 'registred' : user[3]} for user in cursor.execute("SELECT * FROM admins;")}

        conection.commit()
        conection.close()

        return data
    
    def is_user(self, id : int) -> bool:
        return self.users.get(id) != None
    
    def is_admin(self, id : int) -> bool:
        return self.admins.get(id) != None
    
    def registir(self, id : int = None, name : str = None, admin : str = False, region : str = None) -> None:
        name = name.replace("'", '`')
        registred = self.now()
        
        if admin and self.users.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            name = self.users[id]['name']
            cursor.execute(f"INSERT INTO admins (id, name, region, registred) VALUES ({id}, '{name}', '{region}', '{registred}');")
            cursor.execute(f"DELETE  FROM users WHERE id == {id};")

            del self.users[id]
            self.admins[id] = {'name' : name, 'region' : region, 'registred' : registred}
            print(f'New admin {name}')

            conection.commit()
            conection.close()

        elif not admin:
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            if region:
                cursor.execute(f"INSERT INTO users (id, name, region, registred) VALUES ({id}, '{name}', '{region}', '{registred}');") 
                self.users[id] = {'name' : name, 'region' : region, 'registred' : registred}
            else:
                cursor.execute(f"INSERT INTO users (id, name, registred) VALUES ({id}, '{name}', '{registred}');") 
                self.users[id] = {'name' : name, 'region' : None, 'registred' : registred}
                
            print('New user ', name)

            conection.commit()
            conection.close()
        

    def remove(self, id : int = None, admin : bool = False) -> None:
        if admin and self.admins.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            cursor.execute(f"DELETE  FROM admins WHERE id == {id};")
            del self.admins[id]
            
            conection.commit()
            conection.close()

        elif not admin and self.users.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            cursor.execute(f"DELETE FROM users WHERE id == {id};")
            del self.users[id]

            conection.commit()
            conection.close()

    def now(self, zone : str = 'Asia/Tashkent'):
        zone_tz = pytz.timezone(zone)
        zone_time = datetime.now(zone_tz)

        return zone_time.strftime(f"%d.%m.%Y %H:%M")
    

    def update_user_region(self, id : int = None, region : str = None):
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()
        # region = region.replace("'", '')

        cursor.execute(f"UPDATE users SET region = '{region}' WHERE id == {id};")
        self.users[id]['region'] = region 

        conection.commit()
        conection.close()
        
    
    def get_ramadan_info(self, date : str = '2024-3-12', city : str = 'Samarqand') -> dict:
        #SELECT * FROM ramadan WHERE city = 'Samarqand' AND date = '2024-3-12';
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()
        
        for row in cursor.execute(f"SELECT day, start, end, week, week_order, data_id FROM ramadan WHERE city = '{city}' AND date = '{date}';"):
            conection.commit()
            conection.close()
            return {'day' : row[0], 'start' : row[1], 'end' : row[2], 'week' : row[3], 'week_order' : row[4], 'data_id' : row[5]}
        
        conection.commit()
        conection.close()


if __name__ == '__main__':
    db = DataBase()
    db.remove(12)
    db.registir(id = 12, name = "ваьлалвэёёё11```'''dedes", region = None) 
    print(db.users)